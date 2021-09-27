# Practicing defining functions

# pip3 install bs4
# python3
# import bs4

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# opening up connection, grabbing page
my_url = 'https://www.newegg.com/p/pl?d=square+enix'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})
# container = containers[0]


# containers[9] gives you the 10th item down, final fantasy XIV online
# containers contains all the items on the page
# containers[0] gives html, copy and paste into a file.
# use https://www.freeformatter.com/html-formatter.html#ad-output then html file is ready

# file I/O
filename = "games.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)

# containers[0]
for container in containers:
    company = container.div.div.a.img["title"]  # this is what you figure out in html, gets you brand

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text
    # notice how your title_container is within a python list. your title
    shipping_container = container.findAll("li", {"class": "price-ship"})
    if shipping_container == []:
        shipping = ''
    else:
        shipping = shipping_container[0].text.strip()

    print("company" + company)
    print("product name" + product_name)
    print("shipping" + shipping)

    f.write(company + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()
