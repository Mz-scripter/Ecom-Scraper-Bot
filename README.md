# Ecom-Scraper-Bot
A Python-based scraper bot designed to extract product titles and prices from ecommerce sites for data analysis and monitoring.
## eBay Web Scraper
For this project, I utilized Selenium for web automation, selecting "Flash Costume" as the test case. This query had a limited number of pages on eBay, approximately 240 results, which provided better control during the scraping process. Despite the relatively small dataset, the script required 71.7456 seconds to fully execute and save the results to a CSV file. 
The codebase includes two versions: `main_draft.py` with comprehensive inline comments for clarity and `main.py`, a streamlined version without comments for production use.
## Bookscraper
I'm thrilled to share that I just completed my first web scraping project using Scrapy. The performance has been outstanding—it only took 29 seconds to scrape 1,000 results, which is significantly faster than what I experienced with Selenium. Given these results, I'm seriously considering transitioning to Scrapy for my future scraping tasks.
## eBay Web Scraper(scrapy)
I refactored my eBay scraping script, moving from Selenium to Scrapy, and the difference is remarkable. The new Scrapy-based implementation is not only more concise but also exponentially faster. To put it in perspective, Selenium took 71.75 seconds to scrape about 240 results, while Scrapy achieved the same in just 5.98 seconds—nearly 12 times faster. Needless to say, I'm fully transitioning to Scrapy from here on out.
## eBay Scrapy db
Once I successfully made the transition to Scrapy, my next goal was to persist the scraped data into a structured format for easier analysis and management.
To achieve this, I integrated MySQL as the database solution. After installing MySQL, I created a table within my database to store the scraped items. This allowed me to organize the data in a more structured way and perform queries directly on the database as needed. The combination of Scrapy and MySQL proved to be a powerful tool for scraping and managing web data efficiently.
