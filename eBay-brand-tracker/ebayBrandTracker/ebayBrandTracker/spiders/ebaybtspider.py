import scrapy
import requests
import time
from urllib.parse import quote
from fake_useragent import UserAgent


class EbaybtspiderSpider(scrapy.Spider):
    name = "ebaybtspider"
    allowed_domains = ["ebay.com"]
    discord_webhook_url = "https://discord.com/api/webhooks/1306576024682627092/DA5xmfJhqRleDoYE5-KASTsP2C8M0U-W57SQpWAzQm_t3dg6FVuDwU4Y2GtxS9rGpuqh"

    def start_requests(self):
        ua = UserAgent() # Initialize UserAgent
        self.ua = ua # Store UserAgent instance for later use
        # Load brands from brands.txt
        with open('C:/Users/HP/Documents/GitHub/Ecom-Scraper-Bot/eBay-brand-tracker/brand.txt', 'r') as file:
            brands = [line.strip() for line in file.readlines()]
    
        # Generate a search URL for each brand
        for brand in brands:
            headers = {
                'User-Agent': ua.random # Use a random User-Agent for each request
            }
            search_url = f"https://www.ebay.com/sch/i.html?_nkw={quote(brand)}"
            yield scrapy.Request(url=search_url, callback=self.parse, meta={'brand': brand}, headers=headers)

    def parse(self, response):
        brand = response.meta['brand']

        for item in response.css('li.s-item'):
            title = item.css('.s-item__title span::text').get()
            price = item.css('span.s-item__price::text').get()
            link = item.css('a.s-item__link::attr(href)').get()

            # If price is None, follow the item's link to fetch the price
            if price is None and link:
                yield scrapy.Request(url=link, callback=self.parse_item_page, meta={'title': title, 'link': link, 'brand': brand})
            else:
                # Match brand in title as before
                if brand.lower() in (title or "").lower():
                    self.send_discord_notification(brand, title, price, link)
        
        # Check if there is a next page and follow it
        next_page = response.css('a.pagination__next::attr(href)').get()
        if next_page:
            headers = {
                'User-Agent': self.ua.random
            }
            yield scrapy.Request(url=next_page, callback=self.parse, meta={'brand': brand},)
    
    def parse_item_page(self, response):
        price = response.css('span.ux-textspans').get()
        title = response.meta['title']
        link = response.meta['link']
        brand = response.meta['brand']

        self.send_discord_notification(brand, title, price, link)
    
    def send_discord_notification(self, brand, title, price, link):
        # Prepare to send the message to discord
        message = {
            "content": f"**Brand:** {brand}\n"
                       f"**Title:** {title}\n"
                       f"**Price:** {price}\n"
                       f"**Link:** {link}"
        }
        # Send the message using the discord webhook
        response = requests.post(self.discord_webhook_url, json=message,)

        # Check if the message was sent successfully
        if response.status_code == 204:
            self.log(f"Notification sent successfully for {title}")
        
        elif response.status_code == 429:
            retry_after = 10
            self.log(f"Rate limit hit. Retrying after {retry_after} seconds...")
            time.sleep(retry_after)

        else:
            self.log(f"Failed to send notification for {title}. Status code: {response.status_code}")