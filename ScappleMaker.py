__author__ = 'Travis'
import xml.etree.ElementTree as ET
import sys

class ScappleXML:
    """A class for holding and modifying the data of a Scapple XML file"""
    def __init__(self, XMLFile):
        self.tree = ET.parse(XMLFile)
        self.root = self.tree.getroot()

        #list of all IDs which exist
        self.allCurrentIDs = []
        #a dict of all current titles and their associated nodeID
        self.allCurrentTitles = {}
        #The notes connected to each other (regardless of whether it's an arrow or dashed line)
        self.allCurrentConnections = {}
        #The notes which are connected by an arrow. NOTE: The note ID is the origin with the list being the notes it points TO
        self.allCurrentPoints = {}
        self.highestId = 0
        self.loadXML()
        self.activeTitle = ""
        self.activeId = 0

    def loadXML(self):
        #Populate variables...
        for child in self.root[0]:
            self.allCurrentIDs.append(child.attrib.get("ID"))
            if int(child.attrib.get("ID")) > self.highestId:
                self.highestId = int(child.attrib.get("ID"))
            self.allCurrentTitles[child[1].text] = child.attrib.get("ID")
            #Should check here to make sure the ConnectedNoteIDs exists as below with point...
            self.allCurrentConnections[child.attrib.get("ID")] = self.populateCurrentConnections(child[2].text)
            #See if the node is pointing to anything (with the explicit arrow)
            if child.find("PointsToNoteIDs") is not None:
                self.allCurrentPoints[child.attrib.get("ID")] = self.populateCurrentConnections(child.find("PointsToNoteIDs").text)
        #add one to highest to get newest id for new nodes
        self.highestId += 1

        #Is used to populate both current connections and current points
    def populateCurrentConnections(self, connections):
        #list to return
        returnList = []
        #first split along commas
        numbers = connections.split(',')
        #print l
        for n in numbers:
            #for each number, first check if it is hypened
            if "-" in n:
                #if there's a hypen then call expand to get a list of those
                returnList.extend(self.expandNumbers(n))
            else:
                returnList.append(int(n))
        return returnList

        #called if there's a hypen of numbers in the connections.
    def expandNumbers (self, theString):
        r = []
        numbers = theString.split("-")
        for x in range(int(numbers[0]), int(numbers[1])+1):
            r[len(r):] = [x]
        return r

    def createTitle(self, name):
        self.allCurrentTitles[name] = self.highestId
        self.highestId += 1

    #For checking if title exists and setting current id and title to new values
    def checkIfTitleExists(self, name):
        if name in self.allCurrentTitles:
            self.activeTitle = name
            self.activeId = self.allCurrentTitles[name]
            print ("Now adding reference to existing title: {} (ID: {})").format(self.activeTitle, self.activeId)
        else:
            #create title
            self.createTitle(name)
            self.activeTitle = name
            self.activeId = self.allCurrentTitles[name]
            print ("Now adding reference to existing title: {} (ID: {})").format(self.activeTitle, self.activeId)


class InputController:
    """A controller for making things happen from user input."""
    def __init__(self):
        self.XMLFile = sys.argv[1]
        self.lit = ScappleXML(XMLFile)
        self.userinput = raw_input('Title to add references to (type exit to quit, type list to choose from existing titles): ')

    def nextaction(self, input):
        if input.strip() = 'exit'
            self.userinput = 'exit'
        if input.strip() = 'list'
            self.listCurrentTitles()

    def listCurrentTitles(self):



control = InputController()

while control.userinput.strip() != 'exit':
    #ask which title we should work from
    userinput = raw_input('Title to add references to (type exit to quit, type list to choose from existing titles): ')

    if userinput.strip() is 'list':
        #print list and ask for ID
        lit.printList()
        userinput = raw_input('Type ID number to activate text')




    lit.checkIfTitleExists(userinput)