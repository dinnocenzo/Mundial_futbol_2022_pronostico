import pandas as pd
from bs4 import BeautifulSoup
import requests

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
         2018]

year_22 = 2022


def get_matches(year):
    wed = f"https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup"
    response = requests.get(wed)
    content = response.text
    soup = BeautifulSoup(content, "lxml")

    matches = soup.find_all("div", class_="footballbox")

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find("th", class_="fhome").get_text())
        score.append(match.find("th", class_="fscore").get_text())
        away.append(match.find("th", class_="faway").get_text())

    dict_football = {"home": home, "score": score, "away": away, }
    df_football = pd.DataFrame(dict_football)
    df_football["year"] = year
    return df_football


# data historica
fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv("fifa_worldcup_historical_data", index=False)


def get_matches_2022(year_22):
    wed = "https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup"
    response = requests.get(wed)
    content = response.text
    soup = BeautifulSoup(content, "lxml")

    matches = soup.find_all("div", class_="footballbox")

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find("th", class_="fhome").get_text())
        score.append(match.find("th", class_="fscore").get_text())
        away.append(match.find("th", class_="faway").get_text())

    dict_football = {"home": home, "score": score, "away": away, }
    df_football = pd.DataFrame(dict_football)
    df_football["year"] = 2022
    return df_football


df_fixture = get_matches_2022(2022)
df_fixture.to_csv("fifa_worldcup_fixture", index=False)
