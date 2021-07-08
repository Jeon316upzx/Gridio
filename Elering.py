import requests
from bs4 import BeautifulSoup
import sqlite3
from sqlite3 import Error


def create_connection(db_file='Elering.sqlite3'):
    """ 
      create a database connection to the SQLite database
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


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
        conn = create_connection()
        curs = conn.cursor()
        curs.execute("INSERT INTO nordtable".format(row))
        conn.commit()


hourly_prices_one_day_ahead_Estonia(
    "https://dashboard.elering.ee/assets/api-doc.html#/nps-controller")
