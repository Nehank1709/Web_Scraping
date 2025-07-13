from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Open the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals'
driver.get(url)
time.sleep(2)  # Wait for the page to load

# Base XPath to the correct table
table_xpath = "//table[caption[contains(text(),'List of FIFA World Cup finals')]]"

# Number of rows to scrape
max_rows = 10

fifa_data = []
for i in range(2, 2 + max_rows):  # Start from row 2 to skip header
    try:
        year_xpath = f"{table_xpath}//tr[{i}]/th[1]"
        winner_xpath = f"{table_xpath}//tr[{i}]/td[1]"
        score_xpath = f"{table_xpath}//tr[{i}]/td[2]"
        runner_xpath = f"{table_xpath}//tr[{i}]/td[3]"

        year = driver.find_element(By.XPATH, year_xpath).text.strip().split('[')[0]
        winner = driver.find_element(By.XPATH, winner_xpath).text.strip()
        score = driver.find_element(By.XPATH, score_xpath).text.strip().replace('–', ' - ')
        runner_up = driver.find_element(By.XPATH, runner_xpath).text.strip()

        fifa_data.append({
            "year": year,
            "winner": winner,
            "score": score,
            "runners_up": runner_up
        })
    except Exception as e:
        print(f"Row {i} failed to parse: {e}")
        continue

# Convert to JSON
json_data = json.dumps({
    "values": [[d["year"], d["winner"], d["score"], d["runners_up"]] for d in fifa_data]
}, indent=2)

print(json_data)

# Close the browser
driver.quit()
