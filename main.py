import requests
from bs4 import BeautifulSoup
import re
import openai
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

api_key = "YOUR_OPENAI_API_KEY"
openai.api_key = api_key

# Define the list of domains to extract data from
domains = ["https://tonestro.com/", "https://sendtrumpet.com/", "https://www.prewave.com/", "https://twinn.health/", "https://kokoon.io/"]

# Define the user agent header
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"

# Create a session object with the user agent header
session = requests.Session()
session.headers.update({"User-Agent": USER_AGENT})


results = []

def scrape_domain(domain):
    """Scrapes the domain and returns a string of text from all p tags on the home page and the about page."""
    # Make a request to the domain and get the HTML content
    try:
        response = session.get(domain)
        response.raise_for_status()
        html = response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error while requesting {domain}: {e}")
        return None

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html, "lxml")

    # Find all p tags on the page and extract their text
    p_tags = soup.find_all("p")
    p_text = "\n".join([tag.get_text() for tag in p_tags])

    # Find the link that contains the word "about" in the text or href attribute
    link = soup.find("a", text=re.compile("about", re.I), href=re.compile("about", re.I))
    if link:
        # Get the full URL of the link by joining it with the domain
        url = requests.compat.urljoin(domain, link["href"])
        # Make another request to the URL and get the HTML content
        try:
            response = session.get(url)
            response.raise_for_status()
            html = response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Error while requesting {url}: {e}")
            return p_text

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html, "lxml")

        # Find all p tags on the page and extract their text
        p_tags = soup.find_all("p")
        p_text += "\n".join([tag.get_text() for tag in p_tags])

    else:
        logging.info(f"No about page found for {domain}")

    return p_text

def send_message(message_log):
    """Uses OpenAI's ChatCompletion API to get the chatbot's response."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=message_log,  
        max_tokens=800,        
        stop=None,              
        temperature=0.7,        
    )

    # Find the first response from the chatbot that has text in it
    for choice in response.choices:
        if "text" in choice:
            return choice.text

    # If no response with text is found, return the first response's content
    return response.choices[0].message.content

def main():
    """Main function that scrapes each domain and sends the result to the chatbot."""
    for domain in domains:
        # Scrape the domain and get the text from p tags
        p_text = scrape_domain(domain)

        # If the text is not None, append it to the results list
        if p_text:
            results.append(p_text)

    # For each result, send it to the chatbot and print the response
    for i in range(len(results)):
        user_input = results[i]

        message_log = [
            {"role": "user", "content": f"what service or produce does the company offer? what are the name(s) of the founder(s). On a scale of 1 -10, what's a rating for the company based on how it matches any of: Health ,Edtech,Planet Positive, Underrepresented Founders,Financial Inclusion. Return the answer in json format. if no answer, fill with N/A. The service or produce should be a short summary: {user_input}"}
        ]

        response = send_message(message_log)

        print(f"{domains[i]}: {response}")

if __name__ == "__main__":
    main()
