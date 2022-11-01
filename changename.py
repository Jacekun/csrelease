
import re
import os

path: str = os.path.join(".", "app", "build.gradle.kts")
text: str = ""
newAppPackage: str = "com.lagradost.cloudstream3xxx"
findAppId: str = "(?<=applicationId = \")(.*?)(?=\")"

try:
    print("Checking file..")
    if os.path.exists(path):
        # Read contents
        with open(path, "r", encoding='utf-8') as file:
            print("Read file..")
            text: str = file.read()
            #print("Old text => {0}".format(text))
            file.close()
            print("Reading File closed!")
        
        # replace with new content
        with open(path, "w", encoding='utf-8') as file:
            print("Replacing file contents..")
            newText: str = re.sub(findAppId, newAppPackage, text)
            #newText: str = text.replace("com.lagradost.cloudstream3", newAppPackage)
            #print("New text => {0}".format(newText))
            file.truncate(0)
            print("File cleared!")
            file.write(newText)
            print("Done writing!")
            file.close()
            print("File closed!")

except Exception as ex:
    print("Error => {0}: {1}".format(path, ex))
