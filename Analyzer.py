import argparse
import nltk
import spacy
import nbformat
import json
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter
from traitlets.config import Config
import asyncio
import sys

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def init_argparse():

    parser = argparse.ArgumentParser(

        usage="%(prog)s [OPTION] [CHATFILE]",

        description="Analyze a WhatsApp Chat"

    )

    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 0.1"
    )

    parser.add_argument("chatfile",
                        help="The Chatfile")

    parser.add_argument("-i", "--includeNames", action="store_true", default=[],
        help="Include certain Names with Structure ['Name1', 'Name2', ...]")

    parser.add_argument("-e", "--excludeNames", action="store_true", default=[],
        help="Exclude certain Names with Structure ['Name1', 'Name2', ...]")

    return parser


def main():

    parser = init_argparse()

    args = parser.parse_args()
    
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

    try:
        nltk.data.find('corpora/names')
    except LookupError:
        nltk.download('names')

    if spacy.util.is_package("de_core_news_sm") is False:
        spacy.cli.download("de_core_news_sm")


    ChatPath = args.chatfile

    if ChatPath[0] == "\"":
        ChatPath = ChatPath.strip("\"")

    if ChatPath[0] == "\'":
        ChatPath = ChatPath.strip("\'")

    includeNames = args.includeNames
    excludeNames = args.excludeNames

    with open('settings.json', 'w') as f:
        json.dump({"chatPath" : ChatPath, "includeNames" : includeNames, "excludeNames" : excludeNames}, f)

    (body, resources) = runNotebook(openNotebook())

    with open('Analyzer.html', 'w', encoding='utf-8') as f:
        f.write(body)

def get_HTMLExporter():
    c =  Config()
    c.HTMLExporter.exclude_input = True
    c.HTMLExporter.exclude_output_prompt = True
    c.HTMLExporter.exclude_input_prompt = True

    return HTMLExporter(config=c)

def openNotebook():
    with open("NAW.ipynb") as f:
        return nbformat.read(f, as_version=4)

def runNotebook(nb):
    ep = ExecutePreprocessor(timeout=-1)

    ep.preprocess(nb)

    return get_HTMLExporter().from_notebook_node(nb)

if __name__ == "__main__":
    main()
