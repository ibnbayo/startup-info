Startup Information Script
===============

## Overview

This script extracts key information from startup websites about their offerings and founders. It utilizes web scraping and natural language processing to analyze page content and generate information for investors.

Getting it running
------------------

 1. Install Required Packages

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

 2. Install pipenv
 ```bash
pip3 install pipenv
```

 3. Clone the Repository

 ```bash
git clone https://github.com/ibnbayo/startup-info
cd <project_folder>
```

 4. Install Dependencies with pipenv

 ```bash
pipenv install
```
 5. Activate Virtual Environment

```bash
pipenv shell
```

 6. Obtain an [OpenAI API key](https://platform.openai.com) and replace YOUR_OPENAI_API_KEY on line 10 of main.py with it.
```python
api_key = "sk-..."
```

 7. Install requirements
 ```bash
pip install -r requirements.txt
```

 8. Run the script
 ```bash
python main.py
```

## Requirements

- Python 3.6+
- OpenAI API key

## Features

- Scrapes homepages and about/team pages to extract raw content 
- Leverages OpenAI's GPT-3.5 Turbo model for natural language processing
- Structured output containing company offering, founders, and custom ratings/metrics
- Detailed logging and error handling for robustness
- Easily extensible to scrape additional pages and information



## Usage

The script accepts a list of domain names to scrape. It will visit each domain's home page and about page (if found) to extract text content from all `<p>` tags.

This extracted text is then sent to the ChatGPT API with a prompt asking for the company's offerings and founder names. 

ChatGPT's response is printed for each domain.

The script runs the following steps:

1. Accepts list of company domains
2. Scrapes home page and about page (if found) 
3. Extracts text content from `<p>` tags
4. Sends extracted text to ChatGPT API
5. Prints ChatGPT response for each domain


Domains are hardcoded in the script. Edit the `domains` list to scrape different sites.

The OpenAI API key should be set in the script.

## Output

The output will contain ChatGPT's response for each domain with extracted company info in JSON format.

Any errors during scraping will be logged.

## Customization

The prompt sent to ChatGPT can be customized by editing the `message_log` payload in `send_message()`.

Scraping logic can be adapted by changing the `scrape_domain()` function.

Additional parsing steps can be added to extract and structure data before sending to ChatGPT.

## Extending the Scraper

New metrics can be extracted by updating the prompt and extending the output schema.

Advanced functionality like scraping JS-rendered pages, sitemaps crawling, and async requests can be added to scale the scraper.
