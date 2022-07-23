from main_config import MainConfiguration
import requests as req
import json
import pandas as pd

class Helper():
    # We will use this class to write all the functions that will requested by the user directly using the Main class

    def getSoccerPlayerData(playerName):

        playerData = req.get(MainConfiguration.url_endpoint + "?p=" + playerName)
        playerData = json.loads(playerData.content)
        
        if playerData['player'] == None:
            print("Sorry, we could not find the description for this player. Please check the spelling or another famous name this player may also be known as.")
        else:
            playerDescription = playerData['player'][0]['strDescriptionEN']
            print(playerDescription)