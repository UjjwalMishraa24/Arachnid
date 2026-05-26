<img width="1440" height="680" alt="image" src="https://github.com/user-attachments/assets/e1db5c7e-4711-4adb-a7af-81cf723ea669" />

## 🕷️ Arachnid  
A Python-based web scraper that fetches and extracts structured content paragraphs, headings, and normalized URLs from any webpage.  

## Features  

URL Normalization strips query strings and fragments, returning a clean netloc/path form
HTML Content Extraction parses raw HTML and returns all paragraph and headers tag text content
Async-ready built with aiohttp for future async crawling support
Tested unit tests covering both URL normalization and HTML parsing

## Project Structure  

Arachnid
├── crawl.py            
├── main.py             
├── test_crawl.py       
├── pyproject.toml      
└── uv.lock             

## Requirements

Python >= 3.14  
uv (recommended) or pip  

## Installation
Clone the repo and install dependencies:  
bashgit clone https://github.com/UjjwalMishraa24/Arachnid.git  
cd Arachnid  
With uv (recommended):  
bashuv sync  
With pip:  
bashpip install beautifulsoup4 requests aiohttp  
