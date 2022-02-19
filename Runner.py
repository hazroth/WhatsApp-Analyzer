import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter
from traitlets.config import Config

c =  Config()
c.HTMLExporter.exclude_input = True
c.HTMLExporter.exclude_output_prompt = True
c.HTMLExporter.exclude_input_prompt = True

html_exporter = HTMLExporter(config=c)

with open("Analyzer.ipynb") as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=-1)

def run():
    ep.preprocess(nb)

    (body, resources) = html_exporter.from_notebook_node(nb)

    with open('Analyzer.html', 'w', encoding='utf-8') as f:
        f.write(body)

run()