import sys
'''
My Idea is for these two classes just being value classes. The player object will only store their ID/name and
how many baskets their team and the opponent have scored.
The Game class will store a current record of who is on the court for each game. My idea of for another parser
method outside of the class to alter all of it
'''
class Player:
    playerID = ""
    playerName = ""
    teamBaskets = 0
    opponentBaskets = 0
    #IDK which constructor we would use so I made both
    def __init__(self, name):
        self.playerName = name

    def __init__(self, playerID):
        self.playerID = playerID

class Game:
    gameID = ""
    currentPlayers = []
    benchedPlayers = []
    def __init__(self, gameID):
        self.gameID = gameID

#######################################################################################################################
"""
This will be the parser part of the program. We dont need to make it a class and can just throw all of our methods in
here because python is weird.
"""
playByPlay = ""
periodStarters = ""
teamID = ""
def start():
    arguments = sys.argv
    playByPlay = sys.argv[1]
    periodStarters = sys.argv[2]
    teamID = sys.argv[3]


start()
