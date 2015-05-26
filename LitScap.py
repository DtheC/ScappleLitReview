__author__ = 'travis'

#Any node connected by line or arrow is listed in each other's "ConnectedNoteIDs".
# Arrows only appear in the node where the arrow is coming from.
# The node the arrow is pointing to is denoted in the arrow origin's "PointsToNoteIDs"

#The end of the xml document
startOfXML = '<?xml version="1.0" encoding="UTF-8" standalone="no"?><ScappleDocument Version="1.1" ID="FABDC5BC-A7E9-4C97-80B5-3E97BFB9DD81">'
endOfXML = '<NoteStyles><Style Name="Title Text" ID="8D1D7C20-8397-4991-8532-FFFEA410AD11" AffectFontStyle="Yes" AffectAlignment="Yes" AffectTextColor="No" AffectNoteBody="No" AffectFade="No"><FontSize>28.0</FontSize><IsBold>Yes</IsBold></Style><Style Name="Red Text" ID="99579BFA-1ECE-4E67-833E-C91F7AFD7F9C" AffectFontStyle="No" AffectAlignment="No" AffectTextColor="Yes" AffectNoteBody="No" AffectFade="No"><TextColor>1.0 0.0 0.0</TextColor></Style><Style Name="Brown Bubble" ID="A3A70E7A-FA76-4DA5-8A36-337F80F42ADE" AffectFontStyle="No" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="Yes" AffectFade="No"><BorderThickness>1</BorderThickness><BorderColor>0.290055 0.1523 0.182215</BorderColor><FillColor>0.940019 0.892907 0.779716</FillColor></Style><Style Name="Yellow Bubble" ID="96F798C1-0508-4DED-A4B3-13C863EE13E1" AffectFontStyle="No" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="Yes" AffectFade="No"><BorderThickness>1</BorderThickness><BorderColor>0.756763 0.785592 0.373258</BorderColor><FillColor>0.906773 0.910625 0.634363</FillColor>        </Style>        <Style Name="Green Bubble" ID="41D01898-E231-49CE-AD35-5B70BB921C80" AffectFontStyle="No" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="Yes" AffectFade="No">            <BorderThickness>1</BorderThickness>            <BorderColor>0.331867 0.609932 0.356197</BorderColor>            <FillColor>0.790123 0.882327 0.80198</FillColor>        </Style>        <Style Name="Blue Bubble" ID="F93C31ED-5A96-4B71-8AA0-1D7FDDCAF47A" AffectFontStyle="No" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="Yes" AffectFade="No">            <BorderThickness>1</BorderThickness>            <BorderColor>0.477193 0.557066 0.76433</BorderColor>            <FillColor>0.840969 0.866828 0.925903</FillColor>        </Style>        <Style Name="Pink Bubble" ID="B0168266-6688-4F8D-9C6C-345E0FC47567" AffectFontStyle="No" AffectAlignment="No" AffectTextColor="No" AffectNoteBody="Yes" AffectFade="No">            <BorderThickness>1</BorderThickness>            <BorderColor>0.747881 0.366532 0.542813</BorderColor>            <FillColor>0.918452 0.807302 0.863467</FillColor>        </Style>    </NoteStyles>    <UISettings>        <BackgroundColor>0.999737 0.986332 0.931298</BackgroundColor>        <DefaultFont>Helvetica</DefaultFont>        <DefaultTextColor>0.0 0.0 0.0</DefaultTextColor>    </UISettings>    <PrintSettings PaperSize="595.0,842.0" LeftMargin="72.0" RightMargin="72.0" TopMargin="90.0" BottomMargin="90.0" PaperType="iso-a4" Orientation="Portrait" HorizontalPagination="Clip" VerticalPagination="Auto" ScaleFactor="1.0" HorizontallyCentered="Yes" VerticallyCentered="Yes" Collates="Yes" PagesAcross="1" PagesDown="1"></PrintSettings></ScappleDocument>'


#So we need a few things
#a List of all current titles and their associated nodeID
allCurrentTitles = {'first title' : 1, 'second title': 2, 'third title' : 3}
#The notes connected to each other (regardless of whether it's an arrow or dashed line)
allCurrentConnections = {1:[2,3], 2:[1], 3:[1]}
#The notes which are connected by an arrow. NOTE: The note ID is the origin with the list being the notes it points TO
allCurrentPoints = {1:[2]}


#Tak input string and check if it's already a node. If so return the node ID, else return -1
def checkExists(title):
    if title in allCurrentTitles:
        return allCurrentTitles[title]
    else:
        return -1

#append to array
#def append

#Create the actual scapple file
def createFile():
    finalFile = startOfXML
    finalFile += "<Notes>"
    for t, i in allCurrentTitles.iteritems():
        finalFile += '<Note ID="'+str(i)+'" FontSize="12.0" Position="199.0,104.0" Width="57.0"><Appearance><Alignment>Left</Alignment></Appearance><String>'+t+'</String><ConnectedNoteIDs>'
        for c in allCurrentConnections[i]:
            finalFile += str(c)+", "
        finalFile += '</ConnectedNoteIDs><PointsToNoteIDs>'
        if i in allCurrentPoints:
            for p in allCurrentPoints[i]:
                finalFile += str(p)+", "
        finalFile += "</PointsToNoteIDs></Note>"
    finalFile += "</Notes><BackgroundShapes></BackgroundShapes><AutoFit>0-2</AutoFit>"
    print finalFile

createFile()


#load given file and populate variables (allCurrentTitles, allCurrentConnections, allCurrentPoints)

#Ask which title we're currently in and set a global variabel with the name and current id. If title doesn't exist
#then assign new id

#Ask for new connection. If new connection doesn't exist, create it otherwise document a connection/point.

