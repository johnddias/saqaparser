# saqaparser
An HTML parser for SeekingAlpha earnings call transcript Q&amp;A.

Simply provide a valid stock ticker when prompted and you will be provided a list of transcripts to choose from.  Selecting a transcript will parse the transcript Q&A section and output to a file.

## Getting Started

This was written and test using Python 2.7; I do not believe that it will work in Python 3.x.

**Get the source:**

1. Clone the git repository
2. Create a Python virtualenv: `virtualenv venv-saqaparser`
3. Activate it: `source venv-webhookshims/bin/activate`
4.  Install dependencies: `pip -r install requirements.txt`

## Development Notes

* Need to add file output option
* Only finds most recent transcripts due to scrape of SA web page, a "More" option may be useful
