import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup


def extract_session_id(session_str: str):
    match = re.search(r"/seesions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string
    return ""

def perform_search(query):
    try:
        # Set up the browser (assuming Chrome for this example)
        driver = webdriver.Chrome()
        driver.get("https://ahmedabadcity.gov.in/PTAX/DuesSearch")  # Replace with the actual URL

        # Find the input field by its name or other attribute
        input_field = driver.find_element(By.ID, "tenementNo")  # Replace with the actual attribute

        # Type the search query
        input_field.send_keys(query)

        # Press the Enter key (or perform other actions like clicking a button)
        input_field.send_keys(Keys.RETURN)

        # Wait for the page to load (you may need to adjust the sleep time)
        time.sleep(2)

        # You can retrieve information from the page or take screenshots, etc.

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the browser window
        # driver.quit()
        pass

# Example usage
search_query = "05442838390001T"
perform_search(search_query)

# ====================================================

# Replace 'url' with the URL of the website you want to scrape
url = 'https://ahmedabadcity.gov.in/PTAX/DuesSearch'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Assuming the table has a class name 'data-table' (replace with the actual class name)
    table = soup.find('table', class_='table-responsive table-bordered table tabledues bt')

    # Check if the table is found
    if table:
        # Iterate through rows and extract data
        for row in table.find_all('tr'):
            # Extract data from each cell (td)
            columns = row.find_all('td')
            
            # Assuming there are three columns in each row
            if len(columns) <0:
                data1 = columns[0].text.strip()
                data2 = columns[1].text.strip()
                data3 = columns[2].text.strip()
                data4 = columns[3].text.strip()
                data5 = columns[4].text.strip()

                # Print or store the extracted data as needed
                print(f"Data: {data1}, {data2}, {data3}, {data4}, {data5}")
    else:
        print("Table not found on the page.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")