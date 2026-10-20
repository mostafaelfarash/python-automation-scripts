# Python Automation & Utility Scripts 🚀

A collection of useful, lightweight Python automation scripts built to solve real-world tasks, extract data, and organize local workflows efficiently.

---

## 📂 Projects Included

### 1. Simple Web Scraper (Books to Scrape)
* **Description:** A lightweight script that connects to a target website, extracts book titles and prices, cleans the data, and automatically exports it into an organized Excel spreadsheet (`.xlsx`).
* **Technologies:** Python, BeautifulSoup, Requests, Pandas.

### 2. Automated File Organizer
* **Description:** A utility script that cleans up cluttered directories by sorting files into categorized subfolders (Images, Documents, Spreadsheets, Archives, Videos, Audio, and Others) based on their extensions.
* **Technologies:** Python, OS, Shutil.

---

## 🛠️ How to Run Locally

### 1. Prerequisites
Ensure you have **Python** installed on your system.

### 2. Install Required Dependencies
Open your terminal (CMD or PowerShell) and run the following command to install all necessary libraries:
```bash
pip install requests beautifulsoup4 pandas openpyxl
3. Run the Scripts
To run the Web Scraper:

Bash
python scraper.py
(This will generate a scraped_books_data.xlsx file containing the extracted data).

To run the File Organizer:

Bash
python file_organizer.py
git init
git add .
git commit -m "Add Web Scraper and File Organizer automation scripts"
git branch -M main
git remote add origin https://github.com/USERNAME/python-automation-scripts.git
git push -u origin main