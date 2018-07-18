import sys
from collections import namedtuple
'''
My Idea is for these two classes just being value classes. The player object will only store their ID/name and
how many baskets their team and the opponent have scored.
The Game class will store a current record of who is on the court for each game. My idea of for another parser
method outside of the class to alter all of it
Note: named tuples wont work for these because named tuple are immutable
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
playByPlayFile = ""
periodStartersFile = ""
teamID = ""
PlayByPlayTuple = namedtuple('PlayByPlayTuple', 'Game_id Event_Num Event_Msg_Type Period WC_Time PC_Time Action_Type Option1 Option2 Option3 Team_id Person1 Person2 Team_id_type')
PlayByPlayList = []
def start():
    arguments = sys.argv
    playByPlayFile = sys.argv[1]
    periodStartersFile = sys.argv[2]
    teamID = sys.argv[3]
    parse()

def parse():
    """
    So im thinking this method will be the core parsing method. It starts out looking for the first game where the desired
    team is playing and then it takes the starters and adds them to the currently playing lineup. Then it goes through
    the play by play and whenever a shot is made it adds it to the corresponding players. Then when it encounters a new
    period it goes to the period by period starters and updates the currently playing players, and then goes back to the
    play by play. Once the game is over it adds the game to a list of old games, creates a new game, and the process
    continues.
    Im also thinking we immediately go through the files and add everything pertaining to the team to a named tuple. Ie
    two named tuples, one for every period by period involving the team and one for every play by play involving the
    team. That way we dont constantly have the file open cause that might hog up resources.
    :return: lmao nothing
    """
    #Here I basically add all the data from each line to a tuple
    with open(playByPlayFile) as f:
        for line in f:
            splitLine  = line.split()
            play = PlayByPlayTuple(splitLine[0], splitLine[1], splitLine[2], splitLine[3], splitLine[4], splitLine[5],
                                   splitLine[6], splitLine[7], splitLine[8], splitLine[9], splitLine[10], splitLine[11],
                                   splitLine[12], splitLine[13])
            PlayByPlayList.append(play)


start()
