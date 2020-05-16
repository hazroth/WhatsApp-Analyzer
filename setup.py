import nltk
import json as js
import os

print("Downloading needed Language Models")

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('names')

print("\n")
print("Would you like to use Sentiment Analysis (Increases Runtime)? [Y/N]")
sentiment = input()
valid = ["y", "n", "Y", "N"]
while sentiment not in valid:
    print("Please enter either Y or N")
    sentiment = input()
print("Please enter the absolute path to your Chat")
ChatPath = input()

if ChatPath[0] == "\"":
	ChatPath = ChatPath.strip("\"")

if ChatPath[0] == "\'":
	ChatPath = ChatPath.strip("\'")

if sentiment == "y" or sentiment == "Y":
    sentiment = True
else:
    sentiment = False

print("Would you like to save the used Dataframes as Json Files? [Y/N]")
json = input()
while json not in valid:
    print("Please enter either Y or N")
    json = input()
	
if json == "y" or json == "Y":
    json = True
else:
    json = False
	
print("Would you like to save the used Dataframes as CSV Files? [Y/N]")
csv = input()
while csv not in valid:
    print("Please enter either Y or N")
    csv = input()
	
if csv == "y" or json == "Y":
    csv = True
else:
    csv = False

with open('settings.json', 'w') as f:
    js.dump({"sentiment" : sentiment, "chatPath" : ChatPath, "json" : json, "csv" : csv}, f)
	
print("Would you like to run the Software? [Y/N]")
run = input()
while run not in valid:
    print("Please enter either Y or N")
    run = input()

if run == "y" or run == "Y":
    os.system(f"jupyter nbconvert --ExecutePreprocessor.timeout=-1 --no-input --to html --execute Analyzer.ipynb")
