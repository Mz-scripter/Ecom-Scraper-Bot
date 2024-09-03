import scrapy


class EbayspiderSpider(scrapy.Spider):
    name = "ebayspider"
    allowed_domains = ["www.ebay.com"]
    start_urls = ["https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=flash+costume&_sacat=0"]

    def parse(self, response):
        products = response.css('.s-item')

        for product in products:
            yield {
                'product_title': product.css('.s-item__title span::text').get(),
                'product_price': product.css('span.s-item__price::text').get(),
            }
        next_page = response.css('.pagination__next ::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
