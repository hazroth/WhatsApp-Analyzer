import nltk
import json as js
import os

yes = ['Yes', 'YES', 'Y', 'y']
no = ['No', 'NO', 'N', 'n']

print("Downloading needed Language Models")

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('names')

print("\n")

includeNames = []
excludeNames = []

print("Please enter the absolute path to your Chat (Drag and Drop works on most Systems)")
ChatPath = input()

if ChatPath[0] == "\"":
	ChatPath = ChatPath.strip("\"")

if ChatPath[0] == "\'":
	ChatPath = ChatPath.strip("\'")

with open('settings.json', 'w') as f:
    js.dump({"chatPath" : ChatPath, "includeNames" : includeNames, "excludeNames" : excludeNames}, f)
	
print("Would you like to run the Software? [Y/N]")
run = input()
while run not in yes+no:
    print("Please enter either Y or N")
    run = input()

if run in yes:
    os.system(f"jupyter nbconvert --ExecutePreprocessor.timeout=-1 --no-input --to html --execute Analyzer.ipynb")
