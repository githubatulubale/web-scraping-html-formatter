import requests
import re     # regular expression
import bs4    # formatting   
import os     # file path    

url = input("Enter URL:")
response = requests.get(url)
# print(type(response))
# print(response.text)

filename = "temp1.html"
bs = bs4.BeautifulSoup(response.text, "html.parser")
formated_text = bs.prettify()
# print(formated_text)
with open(filename, "w+") as f:
    f.write(formated_text)
    
