# Python-Whatsapp-Analyzer
A small Jupyter Notebook to visualize Whatsapp Chats

# Features

- WordCounts
- WordCloud
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

or depending on your Installation

```
pip3 install -r requirements.txt
```

to install the dependencies (jupyter, matplotlib, pandas, seaborn, textblob_de, nltk, wordcloud, plotly, emoji)

(If the install warns you to add jupyter to your path please do so)

## Setup

To download nltk data and input your settings simply run

```
python setup.py
```

or depending on your Installation

```
python3 setup.py
```

## Configurations

To change settings simply edit the generated settings.json

To optimize the name recognition engine you can exclude and include certain names with **includeNames** and **excludeNames** ``(Use the Python List Syntax)``

# Executing the Program

To run the Program you can either execute setup.py again or run

```
jupyter nbconvert --ExecutePreprocessor.timeout=-1 --no-input --to html --execute Analyzer.ipynb
```

inside your installation folder

# Results

Your Results are saved as **Analyzer.html** in the root directory

