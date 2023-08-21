'''
author@: Nicholas Cali
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Created on 11/10/2019


Hw - 10
'''

import sys

PREF_FILE = "musicrecplus.txt"

userMap = {}
userName = ''
currUser = ''
prefs = []
fileName = "musicrecplus.txt"
file = []


def loadUsers():
    ''' Reads the file for the user namees and returns
        a dictionary with them in it
    '''
    global userMap
    global userName
    global currUser
    global prefs
    global fileName
    global file

    userDict = {}
    try:
        file = open(fileName, 'r')
        for line in file:    
            userName, bands = line.strip().split(":")
            bandList = bands.split(",")
            artists = []
            for x in bandList:
                artists.append(x.strip())
            userDict[userName] = bandList
    except FileNotFoundError:
        file = open(fileName, "w")
        file.close()
    return userDict

def getUserPreferences():
    ''' returns the known user's preferences, if not known it will ask
        what their preferences are
    '''
    global userMap
    global userName
    global currUser
    global prefs
    global fileName
    global file

    newPref = ''
    if userName in userMap:
        prefs = userMap[userName]
        print("I see that you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to see your recommendations:")
    else:
        prefs.clear()
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        newPref = input("that you like:")

    while newPref != "":
        prefs.append(newPref.strip())
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to see your recommendations:")
        
    prefs.sort()
    userMap[userName] = prefs
    return prefs
    

def findBestUser():
    ''' Find the user whose tastes are closest to the current
        user.  Return the best user's name (a string) '''
    global userMap
    global userName
    global currUser
    global prefs
    global fileName
    global file

    users = userMap.keys()
    bestUser = []
    bestScore = -1
    for user in users:
        score = numMatches(prefs, userMap[user])
        if user[-1] != '$':
            if score > bestScore and userName != user and userMap[user]!=userMap[userName]:
                bestUser.clear()
                bestScore = score
                bestUser.append(user)
            elif score == bestScore and userName != user and userMap[user]!=userMap[userName]:
                bestUser.append(user)
    return bestUser

def getRecommendations():
    ''' Gets recommendations for a user (currUser) based
        on the users in userMap (a dictionary)
        and the user's preferences in pref (a list).
        Returns a list of recommended artists.  '''
    global userMap
    global userName
    global currUser
    global prefs
    global fileName
    global file

    bestUser = findBestUser()
    if bestUser == []:
        return []
    recommendations = []
    for x in bestUser:
        recommendations.append(drop(prefs, userMap[x]))
    return recommendations




def drop(list1, list2):
    ''' Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    
    return list3

def numMatches( list1, list2 ):
    ''' return the number of elements that match between
        two sorted lists '''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches
 
    
def saveUserPreferences():
    ''' saves the user prefs to file and closes it, no return.'''
    global userMap
    global userName
    global currUser
    global prefs
    global fileName
    global file

    userMap[userName] = prefs
    file = open(fileName, 'w')
    for user in userMap:
        toSave = str(user) + ":" + "," .join(userMap[user]) + '\n'
        file.write(toSave)
    file.close()
    sys.exit()
   
    
def main():
    global userMap
    global userName
    global currUser
    global prefs
    global fileName
    global file

    userMap = loadUsers()
    
    print("Welcome to the music recommender!")

    userName = input("Please enter a name:")
    print("Welcome,", userName)
   
    
    prefs = getUserPreferences()
    recs = getRecommendations()

    if len(recs) == 0:
        print("I'm sorry but I have no recommendations")
        print("for you right now")
    else:
        print(userName, "based on the users I currently")
        print("know about, I believe you might like:")
        printrecs(recs)

        print("I hope you enjoy them! I will save your")
        print("preferred artists and have new")  
        print("recommendations for you in the future:")

 
    menu()
    
def popular():
    '''prints artists that are like by most users.
       If tie, print all with most likes.
    '''
    lst = popList()
    for x in lst:
        print(x[0])
    menu()
    
def menu():
    '''allows user to naviagate the music recommender'''
    global userMap
    global userName
    global currUser
    global prefs
    global fileName
    global file
    choice = input("Enter a letter to choose an option: \n e - Enter Preferences \n r - Get recommendations \n \
p - Show most popular artists \n h - How popular is the most popular \n m - Which user has the most likes \n q - Save and quit \n \n Your input:")
    
    if choice == 'e':
        prefs.clear()
        prefs = getUserPreferences()
        userMap[userName] = prefs
    if choice == 'r':
        recs = getRecommendations()
        printrecs(recs)
    if choice == 'p':
        popular()
    if choice == 'h':
        howPopular()
    if choice == 'm':
        mostLikes()
    if choice == 'q':
        saveUserPreferences()
    else:
        menu()
    

    

def howPopular():
    '''returns the number of user who like the most popular artists or band.
    '''   
    lst = popList()
    print(lst[0][1])     
    menu()


def popList():
    '''helper for popular'''
    artists = []
    dict = all_artists()
    most = 0
    for x in dict:
        if dict[x] > most:
           artists.clear()
           artists.append([x,dict[x]])
           most = dict[x]
        elif dict[x] == most:
            artists.append([x,dict[x]])
    artists.sort()
    return artists
    

def all_artists():
    '''returns a list of all artists'''
    global userMap
    global userName
    global currUser
    global prefs
    global fileName
    global file

    all_artists = []
    artistDict = {}
    for user in userMap:
        for artist in userMap[user]:
            if user[-1] != "":
                if user[-1] != '$':
                    if artist not in artistDict:
                        artistDict[artist] = 1
                    else:
                        artistDict[artist] += 1
    if artistDict == {}:
        print("Sorry, no artists found")
        menu()
    return artistDict
                  
def mostLikes():
    '''returns the artist with the most likes'''
    global userMap
    global userName
    global currUser
    global prefs
    global fileName
    global file

    userMap = loadUsers()
    x = 0
    y=[]
    for user in userMap:
        if user[-1] != '$':
            if len(userMap[user]) > x:
                y.clear()
                x = len(userMap[user])
            if len(userMap[user]) == x:
                y.append(user)
    for x in y:
        print(x)
    menu()



def printrecs(recs):
    if recs == []:
        print('There are no recommendations at this time')
    else:
        for i in recs:
            for x in i:
                print(x)
    

if __name__ == "__main__":
    main()

