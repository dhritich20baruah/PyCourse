import os
from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)
db = client["test"]
collection = db["jobs"]

folder_path = "job"

file_path = os.path.join(folder_path, f"job.html")

with open(file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

jobs = []

for row in soup.select(""):
    title = row.find("th", class_="nw")
    lastDate = row.select_one("td:nth-child(3) a")
    Post = row.select_one("td:nth-child(5)")
    description = row.select_one("td:nth-child(4)")
    category = row.select_one("td:nth-child(3) a")
    advLink = row.select_one("td:nth-child(5)")
    applyLink = row.select_one("td:nth-child(4)")


