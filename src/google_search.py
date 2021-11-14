
from googlesearch import search

query = "agile risk management 2021"

my_results_list = []
for i in search(query,        # The query you want to run
                tld = 'com',  # The top level domain
                lang = 'en',  # The language
                num = 10,     # Number of results per page
                start = 0,    # First result to retrieve
                stop = 20,  # Last result to retrieve
                pause = 2.0,  # Lapse between HTTP requests
                verify_ssl = False
               ):
    my_results_list.append(i)
    print(i)