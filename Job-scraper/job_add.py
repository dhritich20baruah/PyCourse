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
    title_tag = soup.select_one('div span b') 
    job_title = title_tag.get_text(strip=True) if title_tag else "Unknown Job Title"
    
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
    
    return job_title, combined_text

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
    title, raw_description = process_single_job_html(html_content)
    print(f"  -> Extracted Title: {title}")
    
    # Rephrase
    rephrased_description = rephrase_job_description(raw_description, title)
    print("  -> Rephrasing Complete.")

    # Store in MongoDB
    data_to_save = {
        'title': title,
        'original_description': raw_description,
        'rephrased_description': rephrased_description,
        'date_processed': datetime.datetime.utcnow(),
        'source_file': file_name 
    }
    
    try:
        # collection.insert_one(data_to_save)
        print(data_to_save)
        print(f"  ✅ Successfully stored job: {title} in MongoDB.")
    except Exception as e:
        print(f"  ❌ Failed to store job {title}: {e}")

if __name__ == "__main__":
    main_process()