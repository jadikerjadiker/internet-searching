import requests
from bs4 import BeautifulSoup

search_term = "hiya"
#todo this should just search from the normal US google, not this co.uk one.
goog_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + search_term


r = requests.get(goog_search)

soup = BeautifulSoup(r.text, "html.parser")
for val in [x.text for x in soup.find_all('cite')]:
    print(val)