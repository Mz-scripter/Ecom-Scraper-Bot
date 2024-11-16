# eBay Brand Tracker Scraper

This project is a Scrapy-based web scraper designed to track eBay listings for specific brands. It notifies the user via a Discord webhook whenever a matching listing is found. The brand list is customizable, and the scraper can be configured to run periodically.


## Features

- Scrapes eBay for listings of specified brands.
- Supports tracking multiple brands via a `brands.txt` file.
- Sends notifications to a Discord server with details about the matched listings.
- Handles pagination to retrieve listings across multiple pages.
- Rotates `User-Agent` headers to reduce the chance of detection.


## Setup Instructions

- Python 3.8+
- `pip` package manager
- Scrapy framework installed


### Installation
1. Clone the repository:

 ``` bash
   git clone https://github.com/your-username/ebay-brand-tracker.git
   cd ebay-brand-tracker
 ```
2. Activate Virtual Environment
 source ebay_bt_venv/scripts/activate
3. Install the dependencies:
 pip install -r requirements.txt


## Configuration
1. Brands File
 Update the `brands.txt` file with one brand per line
2. Discord Webhook
 Set your discord webhook URL in the `ebaybtspider.py` file:
 ``` self.discord_webhook_url = "https://discord.com/api/webhooks/your-webhook-id/your-webhook-token" ```


## Running the Scraper
 To start the scraper:
 ``` scrapy crawl ebaybtspider ```


## Example Output
 A sample discord notification:
 ```
    **Brand:** Nike
    **Title:** Nike Air Max 90 shoes
    **Price:** $120
    **Link:** https://ebay.com/itm/example
 ```


## Troubleshooting
 1. No Notifications:
    - Verify your `brands.txt` file and Discord webhook URL.
    - Check Scrapy logs for error
    

