""" Call classes in main class"""
from Classes.ReadPage import ReadPage

print "-" * 50 + "START SYSTEM" + "-" * 50 + "\n"

## Root folder
#
#   pageRank <- Root directory to read
#       |
#       *-->Classes
#       |      |
#       |       *--> *.py
#       |
#       *-->Files
#              |
#              *--> *.txt

#Send root to read file initial value
htmlAnalizer =  ReadPage("./Files/Test.html")

#Call object to ge information
# You can set directory in constructor and function, it's the same
# adn you can use setFile(string) with directory,
#   example :
#   htmlAnalizer =  ReadPage() # Don't sent file directory
#   setFile("./Files/Test.html") # set value, but if you dont like this form
                                # you can set the value when you call countLinks
#   result = htmlAnalizer.countLinks("./Files/Test.html")

result = htmlAnalizer.countLinks()

print "Links encontrados en documentos HTML : ", result.getReferences()
print "Veces que se referencio a si mismo : ", result.getSelfReferences()
print "Links encontrados : "
for e in result.getLinks():
    print e.string
