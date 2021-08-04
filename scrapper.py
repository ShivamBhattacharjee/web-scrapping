from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv 

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/" 
browser = webdriver.Chrome("./chromedriver") 
browser.get(START_URL) 
time.sleep(10)

def scrap():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"] 
    planet_data = []
    soap=BeautifulSoup(browser.page_source,"html.parser")

    for ul_tag in soap.find_all("ul", attrs={"class", "exoplanet"}): 
        li_tags = ul_tag.find_all("li") 
        temp_list = [] 
        for index, li_tag in enumerate(li_tags): 
            if index == 0: 
                temp_list.append(li_tag.find_all("a")[0].contents[0]) 
            else: 
                try: temp_list.append(li_tag.contents[0]) 
                except: temp_list.append("") 
    planet_data.append(temp_list)

    with open("scrapper_2.csv", "w") as f: 
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers) 
        csvwriter.writerows(planet_data)
    
scrap()

