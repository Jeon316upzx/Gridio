import requests
from bs4 import BeautifulSoup
import sqlite3


conn = sqlite3.connect('Nord.sqlite3', check_same_thread=False)


def hourly_prices_one_day_ahead_Estonia(url):
    """
      A simple web scrapper to get 
      get day ahead hourly market prices for Estonia
      Save them to local SQLLite database table
    """

    # using the request make a get request to the url
    r = requests.get(url)

    # using get the content of the html page
    soup = BeautifulSoup(r.content)

    table = soup.findAll()

    for row in table:
        curs = conn.cursor()
        curs.execute("INSERT INTO nordtable".format(row))
        conn.commit()


hourly_prices_one_day_ahead_Estonia(
    "https://dashboard.elering.ee/assets/api-doc.html#/nps-controller")
