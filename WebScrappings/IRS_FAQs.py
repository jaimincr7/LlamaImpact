import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://www.irs.gov/faqs'

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Page loaded successfully")
else:
    print("Failed to retrieve the page")

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

questions = soup.find_all('h4', class_ = 'panel-title')
answers = soup.find_all('div', class_ = 'panel-collapse')

# Initialize an empty list to store the Q&A pairs
faq_data = []

# Loop through the questions and answers to extract and store them
for question, answer in zip(questions, answers):
    # Clean up the text
    question_text = question.get_text(strip=True)
    answer_text = answer.get_text(strip=True)
    
    # Append to faq_data as a dictionary
    faq_data.append({'question': question_text, 'answer': answer_text})

# Print or save the extracted data
for item in faq_data:
    print(f"Question: {item['question']}")
    print(f"Answer: {item['answer']}")
    print('-' * 50)

# Optionally, save data to a file (e.g., JSON)
import json

with open('tax_filing_faq.json', 'w') as f:
    json.dump(faq_data, f, indent=4)

print("FAQ data saved to 'tax_filing_faq.json'")
