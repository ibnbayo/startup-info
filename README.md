Startup Info App
===============

## Overview

This provides investment insights for angel investors. It extracts key information from startup websites about their offerings and founders, and utilizes web scraping and natural language processing to analyse content.

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

This extracted text is then sent to the LLM API with a prompt asking for the company's offerings and founder names. 

LLM's response is printed for each domain.

The script runs the following steps:

1. Accepts list of company domains
2. Scrapes home page and about page (if found) 
3. Extracts text content from `<p>` tags
4. Sends extracted text to LLM API
5. Prints LLM response for each domain


Domains are hardcoded in the script. Edit the `domains` list to scrape different sites.

The OpenAI API key should be set in the script.

## Output

The output will contain the LLM's response for each domain with extracted company info in JSON format.

Any errors during scraping will be logged.

## Customization

The prompt sent to LLM can be customized by editing the `message_log` payload in `send_message()`.

Scraping logic can be adapted by changing the `scrape_domain()` function.

Additional parsing steps can be added to extract and structure data before sending to ChatGPT.

## To Do
- Batch requests to OpenAI API to avoid getting rate-limited due to free tier limitations.



## Extending the solution

#### Advanced Data extraction
- Scrape dynamic content using a headless browser or JavaScript engine to execute scripts on page and render HTML content before parsing with BeautifulSoup.

- Extract data from other pages or similar pages with varying names.

#### Additional Data Sources

- Incorporate data from Crunchbase to get more structured founder, funding, and category data
- Use Google search results to find additional pages and sources about the company and founders
- Access Alexa or SimilarWeb to get traffic and engagement metrics for each site

#### More Advanced Extraction

- Use more advanced NLP techniques like named entity recognition to identify founders, products, etc.
- Build a categorization model to classify companies into sectors like health, edtech, etc.
- Use sentiment analysis to gauge positive/negative language on site as a proxy for company reception

#### Additional Analysis

- Expand criteria analysis to include more categories and finer granularity
- Include scoring system that ranks companies across multiple categories and metrics
- Visualize company ratings and extracted information in a dashboard


#### Testing & Maintenance

- Write unit tests for individual modules 
- Implement integration testing framework across full data pipeline
- Build repeatable processes to catch site changes and maintain scraper 


## Exploratory

- Combine internet data with information from parsed pitch decks in relational database for structured scouting
- Create visual representations (graphs, charts) based on data obtained, aiding investors in quick comprehension
