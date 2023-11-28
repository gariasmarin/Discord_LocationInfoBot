import requests
from bs4 import BeautifulSoup
import wikipedia
from transformers import pipeline
import time
from datetime import datetime, timedelta

# import pywikibot
# site = pywikibot.Site('en', 'wikipedia')


# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
#
# abstract = wikipedia.summary("Raleigh, North Carolina")
#
# print(summarizer(abstract, max_length=250, min_length=100, do_sample=False))


raleigh = wikipedia.WikipediaPage(title="Raleigh, North Carolina", preload=True)
print(raleigh.sections)
