__author__ = 'Travis'

import xml.etree.ElementTree as ET


tree = ET.parse('pythontest.scap')
root = tree.getroot()

#So we need a few things
#a List of all current titles and their associated nodeID
#allCurrentTitles = {'first title' : 1, 'second title': 2, 'third title' : 3}
#The notes connected to each other (regardless of whether it's an arrow or dashed line)
#allCurrentConnections = {1:[2,3], 2:[1], 3:[1]}
#The notes which are connected by an arrow. NOTE: The note ID is the origin with the list being the notes it points TO
#allCurrentPoints = {1:[2]}


#So we need a few things
#a List of all current titles and their associated nodeID
allCurrentTitles = {}
#The notes connected to each other (regardless of whether it's an arrow or dashed line)
allCurrentConnections = {}
#The notes which are connected by an arrow. NOTE: The note ID is the origin with the list being the notes it points TO
allCurrentPoints = {}

#activeTitle is the cureent title we are adding refs to. currentID is the title's id
activeTitle = ""
activeId = ""

#utility variables
#highestId holds the next value which is unused in the current nodes. This is assigned to any new nodes created (then 1 is added)
highestId = 0

#Is used to populate both current connections and current points
def populateCurrentConnections(connections):
    #list to return
    returnList = []
    #first split along commas
    l = connections.split(',')
    #print l
    for n in l:
        #for each number, first check if it is hypened
        if "-" in n:
            #if there's a hypen then call expand to get a list of those
            returnList.extend(expandNumbers(n))
        else:
            returnList.append(int(n))
    return returnList

#called if there's a hypen of numbers in the connections.
def expandNumbers (theString):
    r = []
    l = theString.split("-")
    for x in range(int(l[0]), int(l[1])+1):
        r[len(r):] = [x]
    return r

#Populate variables...
for child in root[0]:
    if int(child.attrib.get("ID")) > highestId:
        highestId = int(child.attrib.get("ID"))
    allCurrentTitles[child[1].text] = child.attrib.get("ID")
    #Should check here to make sure the ConnectedNoteIDs exists as below with point...
    allCurrentConnections[child.attrib.get("ID")] = populateCurrentConnections(child[2].text)
    #See if the node is pointing to anything (with the explicit arrow)
    if child.find("PointsToNoteIDs") is not None:
        allCurrentPoints[child.attrib.get("ID")] = populateCurrentConnections(child.find("PointsToNoteIDs").text)
#add one to highest to get newest id for new nodes
highestId += 1

def createTitle(name):
    global highestId
    allCurrentTitles[name] = highestId
    highestId += 1

#For checking if title exists and setting current id and title to new values
def checkIfTitleExists(name):
    global activeId
    if name in allCurrentTitles:
        activeId = allCurrentTitles[name]
        print ("Now adding reference to existing title: {} (ID: {})").format(activeTitle, activeId)
    else:
        #create title
        createTitle(name)
        activeId = allCurrentTitles[name]
        print ("Now adding reference to existing title: {} (ID: {})").format(activeTitle, activeId)

#Ask which title we're currently in and set a global variabel with the name and current id. If title doesn't exist
#then assign new id

activeTitle = input('Title to add references to: ')

#Ask for new connection. If new connection doesn't exist, create it otherwise document a connection/point.
checkIfTitleExists(activeTitle)

print ("Now adding reference to existing title: {} (ID: {})").format(activeTitle, activeId)
print allCurrentTitles


