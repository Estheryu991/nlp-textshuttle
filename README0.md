### Task 1: Corpus Cleaning

A corpus is a collection of text segments, each consisting of a single string. 

On disk, corpora are often stored in line-delimited plain text files containing one segment per line.

Before training NLP models, corpora – often crawled from the web and thus containing noise – must be cleaned. 

__Implement two cleaning methods: filtering and punctuation normalization.__

Implement the `filter` and `normalize` methods in `preprocess_corpus.py` according to their docstring specifications. 

Use the file stored in `data/pro-fr.txt` for testing.


# Filtering: 
Refer to this [document about docstrings and standards](https://pandas.pydata.org/docs/development/contributing_docstring.html)

# Punctuation Normalization: 

### Task 2: Use of REST API

Some NLP models operate on the level of sentences, but a segment in a corpus may contain multiple sentences. 

__Implement the `split` method in `preprocess_corpus.py` to split up such segments into single sentences, as specified in the docstring.__

Sentence splitting are complex. 

Use our REST API as described [here](https://stg.tait.ts.mt/api/v2/docs) 
(Ignore the details about authentication as the `/split_sentences` endpoint allows __unauthenticated requests__).

Use the [`requests` module](https://pypi.org/project/requests/) to communicate with the online service. 
This module is not part of Python's standard library; Install 

### Task 3: Command Line Interface

__Implement a command line interface (CLI) in `preprocess_corpus.py`__ . 
Apply the functionality implemented in tasks 1 and 2 to a corpus stored on disk. 
The CLI should load a corpus; then apply 

>>>(1) sentence splitting, 
>>>(2) filtering, 
>>>(3) normalization, 
>>> Write all processed segments to the standard output. 

The CLI should accept two options `--min-alpha` and `--language` to control the respective parameters.


# Examples:

```
$ python3 preprocess_corpus.py data/corpus.de.txt
Wie geht's?
Ausgezeichnet.
Und dir?
...
$ python3 preprocess_corpus.py --min-alpha 0.9 data/corpus.de.txt
Ausgezeichnet.
...
```
