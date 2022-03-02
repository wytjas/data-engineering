#Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas:
import pandas as pd
from bs4 import BeautifulSoup 
import requests

url = "https://en.wikipedia.org/wiki/World_population"
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

#looking for the 10 most densly populated countries table:
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)
print(tables[table_index].prettify())

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

#put scraped data into a dataframe: 
pd.read_html(str(tables[5]), flavor='bs4')
population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]
