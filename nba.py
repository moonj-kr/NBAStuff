playByPlay="Play by Play Data Sample"
eventCodes="Event Codes"
lineUp="Game Lineup Data Sample"
playlst=[] #play by play
eventlst=[] #events
lineuplst=[] # lineup

# reads files and stores to according lists
def read(name,lst):
    file = open(name)
    line = file.readline().strip()
    while line != "":
        splitLine = line.split("\t")
        lst.append(splitLine)
        line = file.readline().strip()
        print(line)
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

    # adding plus/minus to players
    scoringTeam = playlst[10] #scoring team id
    for event in playlst:
        print(event)
        print("here")
        if event[2] == '1':
            # if there is a goal
            print("true")
            # find team id







#       if(event==1):
 #           for player,list in players:
  #
   #             print(player)
    #            print("WEIOFFFFFFFFFFFFIEWOFIJEI")
     #           print(list[0])
      #          print(scoringTeam)
       #         if list[0] == scoringTeam:
        #            print(list)
         #           list[1] += 1
          #          print(list)
           #         print("wut")
            #pass
            #do plus/minus


main()