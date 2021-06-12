import json
import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

a = range(2014,2021)
b = ["EPL", "La_liga", "Bundesliga", "Serie_A", "Ligue_1"]

league_run = 0

for j in b:
    championship = "https://understat.com/league/"+str(j)+"/"
    loop_run = 0
    league_run += 1
    for i in a:
        season = i
        loop_run += 1
        url = championship+str(i)
        print(url)
        
        page_connect = urlopen(url)
        page_html = bs(page_connect, 'html.parser')

        data_string = str(page_html.findAll(name="script")[3])
        
        start_ind = data_string.index("('")+2
        end_ind = data_string.index("')")

        json_data = data_string[start_ind:end_ind]
        json_data = json_data.encode("utf8").decode("unicode_escape")
        #print(json_data)

        final_json = json.loads(json_data)
        #print(final_json)

        data = pd.json_normalize(final_json)
        data.insert(loc=0, column="season", value=season)

        # Convert data types to appropriate dtypes
        convert_dict = {'id': int,
                        'player_name': str,
                        'games': int,
                        'time': int,
                        'goals': int,
                        'xG': float,
                        'assists': int,
                        'xA': float,
                        'shots': int,
                        'key_passes': int,
                        'yellow_cards': int,
                        'red_cards': int,
                        'position': str,
                        'team_title': str,
                        'npg': int,
                        'npxG': float,
                        'xGChain': float,
                        'xGBuildup': float
                        }
        data = data.astype(convert_dict)
        data.insert(0, "League_Name", str(j))
        #writing to csv
        league = str(j) + ".csv"
        if loop_run == 1:
            data.to_csv(league, index=False)
        else:
            data.to_csv(league, mode='a', header=False, index=False)
    if league_run == 1:
        df = pd.read_csv(league)
    else:
        df_other = pd.read_csv(league)
        df = df.append(df_other)
print(df.head())
print(df.tail())
df.to_csv("Final_Data.csv", index=False)

print("Status: Completed")
