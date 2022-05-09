import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'glasses_offers'
    allowed_domains = ['https://www.glassesshop.com/']


    def start_requests(self):
        yield scrapy.Request(url='https://www.glassesshop.com/bestsellers', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
        })

    def parse(self, response):
        rows = response.xpath("//ul[@id='product-lists']/div/").get()
        print(rows)
        # for product in response.xpath("//ul[@id='product-lists']/div/"):
        #     yield {
        #         'title': product.xpath(".//a[@class='product-title p-tab p-tab-15473']/text()").get(),
        #         # 'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
        #         # 'discoutned_price': product.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
        #         # 'original_price': product.xpath(".//div[@class='p_box_price']/span[2]/text()").get(),
        #         # 'User-Agent': response.request.headers['User-Agent']
        #     }


        # next_page = response.xpath("//a[@class='nextPage']/@href").get()
        #
        #
        # if next_page:
        #     yield scrapy.Request(url=next_page, callback=self.parse, headers={
        #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
        #     })
