playByPlay="Play by Play Data Sample"
eventCodes="Event Codes"
lineUp="Game Lineup Data Sample"
playlst=[]
eventlst=[]
lineuplst=[]



# reads files and stores to according lists
def read(name,lst):
    file = open(name)
    line = file.readline()
    line = file.readline().strip()
    while line != "":
        splitLine = line.split("\t")
        lst.append(splitLine)
        line = file.readline().strip()
    file.close()


def main():
    read(playByPlay,playlst)
    read(eventCodes,eventlst)
    read(lineUp,lineuplst)
    print(eventlst)
    # intializing the dict of players with their team id and plus/minus
    players=dict()
    for player in lineuplst[2]:
        players[player]=[lineuplst[3],0]
    for event in playlst[2]:
        if(event==1):
            #do plus/minus


main()