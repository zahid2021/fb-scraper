import json
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

PAGE_URL = "https://www.facebook.com/PixarCars"
MAX_POSTS = 5

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# Step 1: Open Facebook
driver.get("https://www.facebook.com")
time.sleep(3)

# Step 2: Load cookies
with open("cookies.json", "r") as f:
    cookies = json.load(f)

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
time.sleep(5)

# Step 3: Go to PixarCars page
driver.get(PAGE_URL)
time.sleep(6)

# Step 4: Scroll to load posts
for _ in range(6):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

# Step 5: Collect post links
posts = driver.find_elements(By.XPATH, "//a[contains(@href,'/posts/')]")
post_links = []

for p in posts:
    link = p.get_attribute("href")
    if link and link not in post_links:
        post_links.append(link)
    if len(post_links) >= MAX_POSTS:
        break

print(f"Found {len(post_links)} posts")

all_data = []

# Step 6: Visit each post
for idx, post_url in enumerate(post_links, 1):
    print(f"Scraping post {idx}: {post_url}")
    driver.get(post_url)
    time.sleep(6)

    # Scroll comments
    for _ in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    # Extract comments
    comments = driver.find_elements(By.XPATH, "//div[@role='article']//div[@dir='auto']")
    comment_texts = [c.text.strip() for c in comments if c.text.strip()]

    # Extract like count
    likes = "0"
    try:
        likes = driver.find_element(By.XPATH, "//span[contains(text(),'like')]").text
    except:
        pass

    for c in comment_texts:
        all_data.append({
            "post_url": post_url,
            "likes": likes,
            "comment": c
        })

# Step 7: Save CSV
df = pd.DataFrame(all_data)
df.to_csv("pixar_cars_comments.csv", index=False, encoding="utf-8")

print("Mission accomplished. Data saved to pixar_cars_comments.csv")

driver.quit()
