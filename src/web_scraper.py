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
# print(results.prettify())

python_jobs = results.find_all("h2", string="Python")
print(python_jobs)
#TODO Pick a useful agile info page to scrape

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# extract all the job elements inthe page
job_elements = results.find_all("div", class_="card-content")

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    links = job_element.find_all("a")
    print(" List of links")
    print(links)
    for link in links:
        print("actual link")
        print(link)
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
    print()

#print(page.text)