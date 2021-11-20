# Practice scraping wewb content with requests and beautiful soup 4

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

"""
 The element you’re looking for is a <div> with an id attribute that has the value "ResultsContainer". 
 It has some other attributes as well, but below is the gist of what you’re looking for:
"""
results = soup.find(id="ResultsContainer")
print(results.prettify())

python_jobs = results.find_all("h2", string="Python")
print(python_jobs)
#TODO Pick a useful agile info page to scrape

# extract all the job elements inthe page
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

#print(page.text)