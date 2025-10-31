import os
from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

# Country mapping
country_map = {
       11:"Wallis_and_Futuna",
       12: "Yemen",
       13: "Zambia",
       14: "Zimbabwe",
       15: "The_Cook_Islands"
}

# MongoDB connection
client = MongoClient(MONGO_URI)
db = client["test"]
collection = db["holidays"]

# Folder path where HTML files are stored
folder_path = "holidays"

# Loop through files holiday_0.html to holiday_6.html
for key in country_map:
    file_path = os.path.join(folder_path, f"holiday_{key}.html")
    country = country_map[key]

    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    holidays = []

    # Loop through table rows
    for row in soup.select("#holidays-table tbody tr"):
        raw_date = row.find("th", class_="nw")
        name_tag = row.select_one("td:nth-child(3) a")
        details_tag = row.select_one("td:nth-child(5)")
        type_tag = row.select_one("td:nth-child(4)")

        if not raw_date or not name_tag:
            continue

        raw_date = raw_date.text.strip()
        name = name_tag.text.strip()
        details = details_tag.text.strip() if details_tag else ""

        if details:
            type_value = f"{type_tag.text.strip()} ( {details} )"
        else:
            type_value = type_tag.text.strip()

        date_parts = raw_date.split(" ")
        if len(date_parts) == 2:
            day, month_short = date_parts
            month_map = {
                "Jan": "January", "Feb": "February", "Mar": "March",
                "Apr": "April", "May": "May", "Jun": "June",
                "Jul": "July", "Aug": "August", "Sep": "September",
                "Oct": "October", "Nov": "November", "Dec": "December"
            }
            month_full = month_map.get(month_short, month_short)
            formatted_date = f"{month_full} {day}"
        else:
            formatted_date = raw_date

        holidays.append({
            "country": country,
            "date": formatted_date,
            "name": name,
            "type": type_value,
            "year": 2026,
            "aliases": []
        })

    if holidays:
        collection.insert_many(holidays)
        print(f"{country} holidays inserted successfully!")
    else:
        print(f"No holidays found for {country}.")

print("✅ All files processed.")
