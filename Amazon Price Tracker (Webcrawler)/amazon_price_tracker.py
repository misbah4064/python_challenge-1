import requests
from bs4 import BeautifulSoup
# you need to install requests, bs4 and lxml
# URL holds the link of the amazon product you want to track
URL = 'https://www.amazon.com/Dell-Desktop-i7-9700-GeForce-i5090-7166GRY-PUS/dp/B07X6BR5W3/ref=sr_1_35?dchild=1&keywords=dell+tower+2000&qid=1590859610&sr=8-35'

# you'll need to provide your own User-Agent, by simply going to google and search for "my User-Agent"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'}

#requests gets the content of the URL and saves it in our page variable
page = requests.get(URL,headers = headers)

# we are using Beautiful Soup to parse the content
soup = BeautifulSoup(page.text,'lxml') #make sure you use "lxml' or "html5lib" parser instead of "html.parser"
price_text = soup.find(id= "priceblock_ourprice").get_text(strip = True).replace('$','').replace(',','')
price = float(price_text)
#print("price = "+str(price))

if price < 1250:
	print ("Hey, the price is low, and the price is: "+ str(price))
