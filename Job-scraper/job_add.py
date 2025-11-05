import os
import re
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pymongo import MongoClient
from google import genai
from google.genai.errors import APIError
import datetime

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

try:
    client = MongoClient(MONGO_URI)
    db = client["test"]
    collection = db["jobs"]
except Exception as e:
    print(f"FATAL: Could not connect to MongoDB. Error: {e}")
    exit()
     
try:
    # Gemini Client (Initializes automatically if GEMINI_API_KEY is in environment)
    ai_client = genai.Client()
except Exception as e:
    print(f"FATAL: Could not initialize Gemini Client. Check GEMINI_API_KEY. Error: {e}")
    exit()

def rephrase_job_description(content_text, job_title):
    """Calls Gemini API to clean and rephrase the job content."""
    prompt = (
        f"You are a professional copywriter specializing in modern job postings. "
        f"The job title is: {job_title}. "
        f"Analyze the following raw job content and rephrase it into a clear, professional, and engaging job description. "
        f"Use appropriate headings (like 'Summary', 'Qualifications', 'Stipend', 'How to Apply'). "
        f"Crucially, **remove all unnecessary boilerplate, HTML remnants, and specific dates** (like '14th October 2025' or '31st March, 2024') that are not part of a requirement list. "
        f"Return ONLY the cleaned and rephrased job description text.\n\n"
        f"Raw Content:\n\n---\n{content_text}\n---"
    )

    try:
        response = ai_client.models.generate_content(
            model='gemini-2.0-flash', # Switched to 2.5-flash for speed/cost
            contents=prompt
        )
        print(response)
        return response.text.strip()
    except APIError as e:
        print(f"  ❌ Gemini API Error for job {job_title}: {e}")
        return f"[Rephrase Failed]: {content_text[:100]}..."
    except Exception as e:
        print(f"  ❌ General AI Error for job {job_title}: {e}")
        return f"[Rephrase Failed]: {content_text[:100]}..."
    
def process_single_job_html(html_content):
    """Extracts title and cleans the text from a single HTML string."""
    soup = BeautifulSoup(html_content, "html.parser")

    # Attempt to extract title (Assuming it's in a prominent bold span near the start)
    # container = soup.find_all('div', class_='job-post-container')
    title_tag = soup.select_one('#PostBody > div:nth-of-type(1) span') 
    job_title = title_tag.get_text(strip=True) if title_tag else "Unknown Job Title"

    date_tag = soup.select_one('span > b')
    pattern = r'^Last Date:\s*\.?'
    date_string = date_tag.get_text(strip=True) if date_tag else "N/A"
    last_date_str = re.sub(pattern, '', date_string, flags=re.IGNORECASE).strip()

    # --- B. Link Extraction ---
    links = {
        "online_application_forms": [],
        "advertisement_details": [],
        "official_website": []
    }

    tbody = soup.find('tbody')
    if tbody:
        for row in tbody.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) == 2:
                label_text = columns[0].get_text(strip=True)
                link_tag = columns[1].find('a')

                if link_tag and link_tag.has_attr('href'):
                    href = link_tag['href']

                    if "Online Application Form" in label_text:
                        links["online_application_forms"].append(href)
                    elif "Advertisement Details" in label_text:
                        links["advertisement_details"].append(href)
                    elif "Official Website" in label_text:
                        links["official_website"].append(href)
    
    # ------------------ Cleaning Steps ------------------
    # Remove known junk tags first
    for unwanted_tag in soup(['script', 'style', 'iframe', 'ins', 'center', 'br', 'style']):
        unwanted_tag.decompose()

    # Aggregate text from all relevant justified divs
    content_divs = soup.find_all('div', style=lambda value: value and 'text-align: justify' in value)
    full_text_list = []

    for div in content_divs:
        text = div.get_text(strip=True, separator=' ')
        if text.strip():
            full_text_list.append(text.strip())

    combined_text = "\n\n".join(full_text_list)
    
    # Final regex cleaning
    combined_text = re.sub(r'[ \t]+', ' ', combined_text)
    combined_text = re.sub(r'\n{3,}', '\n\n', combined_text).strip()
    combined_text = combined_text.replace('&amp;', '&')
    
    return job_title, last_date_str, combined_text, links

def main_process(folder_path="job"):
    """Iterates through HTML files, processes them, and stores results."""
    
    # Simulate processing multiple files in the 'job' folder
    # In a real scraper, you would iterate over scraped HTML content strings
    
    # For this example, we'll only process the hardcoded file as in your input:
    file_name = "job.html"
    file_path = os.path.join(folder_path, file_name)

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}. Exiting.")
        return

    print(f"Processing file: {file_name}")

    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    
    # Extract and clean
    title, last_date_str, raw_description, job_links = process_single_job_html(html_content)
    # print(f"  -> Extracted Title: {title}")
    
    # Rephrase
    rephrased_description = rephrase_job_description(raw_description, title)
    # print("  -> Rephrasing Complete.")

    

    posts_match = re.search(r'No of posts:.*?(\d+)\s+posts', raw_description, re.IGNORECASE)
    total_posts = int(posts_match.group(1)) if posts_match and posts_match.group(1).isdigit() else 0

    # Store in MongoDB
    data_to_save = {
        'title': title,
        'lastDate': last_date_str, 
        'Post': total_posts,
        'description': rephrased_description,
        'category': 'Assam Health Infrastructure Development & Management Society',
        'advLink': job_links['advertisement_details'][0] if job_links['advertisement_details'] else None,
        'applyLink': job_links['online_application_forms'][0] if job_links['online_application_forms'] else None,
        'createdAt': datetime.datetime.utcnow(),
    }
    
    try:
        collection.insert_one(data_to_save)
        # print(data_to_save)
        print(f"  ✅ Successfully stored job: {title} in MongoDB.")
    except Exception as e:
        print(f"  ❌ Failed to store job {title}: {e}")

if __name__ == "__main__":
    main_process()