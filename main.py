from helper import Helper

class Main():
    # This is the main class. This is the class which gives this small project its user interaction.
    # This class also calls the function within the Helper class which calls the API
    
    playerName = input('Which player do you want to know about? : ')

    try:
        int(playerName)
        input("Please enter the name of the player you are searching for in characters : ")
    except:
        Helper.getSoccerPlayerData(playerName)
    
