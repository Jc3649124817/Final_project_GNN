import requests
import json
from time import sleep
import time


if __name__ == "__main__":
        
    mykey = "RGAPI-9a78a42b-2197-4ea7-bbf6-9e2aa75735bb"
    match_region = "EUW1_"
    #matchID = "NA1_5184712521"
    match_num = 7223755421

    time_init = time.time()

    headers = {
        "X-Riot-Token": mykey
    } 

    matches_found = 0

    while True:
        time1 = time.time()
        match_id = match_region  + str(match_num)
        url = f'https://europe.api.riotgames.com/tft/match/v1/matches/{match_id}'
        response = requests.get(url, headers=headers)

        match_num +=3


        if response.status_code == 200:
            # Get the JSON data from the response
            data = response.json()

            # Save the data to a JSON file
            file_string = "./json_files/" + match_id + ".json"
            with open(file_string, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            
            matches_found+=1
            time_elapsed = time.time() - time_init
            if matches_found % 100 == 0:
                print(f'{matches_found} matches found in {time_elapsed} seconds')
            print("Match data saved successfully.")
            
        elif response.status_code == 429:
            print("sleeping for 70 seconds")
            sleep(70)
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
        print(time.time() - time1)

    

