# Facebook Scraper

A Selenium-based Python scraper that extracts posts and comments from Facebook pages.

---

## 📋 What It Does

- Logs into Facebook using saved cookies
- Navigates to a target Facebook page (e.g. Pixar Cars)
- Scrolls to load posts automatically
- Visits each post and extracts comments
- Saves all data to a CSV file

---

## 📁 Project Structure
```
fb-scraper/
├── fb_scraper.py        # Main scraper script
├── cookies.json         # Facebook session cookies
├── pixar_cars_comments.csv  # Output CSV file
```

---

## ⚙️ Installation
```bash
pip install selenium pandas
```

---

## 🚀 Usage
```bash
python fb_scraper.py
```

---

## ✨ Features

- ✅ Cookie-based login (no password needed)
- ✅ Auto-scroll to load more posts
- ✅ Extracts comments and like counts
- ✅ Saves data to CSV

---

## 🛠️ Tech Stack

Python · Selenium · Pandas · ChromeDriver
