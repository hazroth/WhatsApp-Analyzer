# Python-Whatsapp-Analyzer
A small Jupyter Notebook to visualize Whatsapp Chats

# Features

- WordCounts
- Name Frequency
- Emoji Frequency
- Time of Day Frequency
- Who sends the most Messages
- Who sends the most Media
- Who sends the longest Messages
- Who Answers Who Snakey Graph

# Requirements

Make sure you have a current version of **Python 3** and **pip** installed

**(Not compatible with Python 2)**


# Installation

First Clone this Repository into a Folder of your choosing

After that open a Terminal in your cloned repository folder

## Dependencies

In said folder execute the following command

```
pip install -r requirements.txt
```

to install the dependencies (jupyter matplotlib pandas nltk spacy plotly emoji demoji numpy)

# Running the Program

Executing the Python Script will also install needed Language Models

```
usage: Analyzer.py [OPTION] [CHATFILE]

Analyze a WhatsApp Chat

positional arguments:
  chatfile            The Chatfile

options:
  -h, --help          show this help message and exit
  -v, --version       show program's version number and exit
  -i, --includeNames  Include certain Names with Structure ['Name1', 'Name2', ...]
  -e, --excludeNames  Exclude certain Names with Structure ['Name1', 'Name2', ...]
```

# Results

Your Results are saved as **Analyzer.html** in the root directory

