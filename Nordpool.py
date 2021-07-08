import requests
from bs4 import BeautifulSoup
import sqlite3


conn = sqlite3.connect('Nord.sqlite3', check_same_thread=False)


def hourly_prices_one_day_ahead_Finland(url):
    """
      A simple web scrapper to get 
      day ahead hourly market prices 
      for Finland. Save them to local SQLLite database table
    """

    # using the request make a get request to the url
    r = requests.get(url)

    # using get the content of the html page
    soup = BeautifulSoup(r.content)

    table = soup.find("table", {'id': "datatable"})

    for row in table.findAll("tr"):
        curs = conn.cursor()
        curs.execute("INSERT INTO nordtable".format(row))
        conn.commit()


hourly_prices_one_day_ahead_Finland(
    "https://www.nordpoolgroup.com/Market-data1/#/nordic/table")
