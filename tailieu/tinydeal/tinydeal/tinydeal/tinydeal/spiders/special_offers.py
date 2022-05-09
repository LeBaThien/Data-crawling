# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['web.archive.org']

    # mỗi lần chạy nó sẽ cần request lại header,
    # header này có thể tìm bằng cách search gg
    # vào page đang crawl, => f12 => network => click all, maybe you see it
    def start_requests(self):
        yield scrapy.Request(url='https://web.archive.org/web/20190324163700/http://www.tinydeal.com/specials.html', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
        })

    # Hàm sẽ trả về tất cả các yêu cầu crawl trên 1 trang
    def parse(self, response):
        for product in response.xpath("//ul[@class='productlisting-ul']/div/li"):
            yield {
                'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                'discoutned_price': product.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
                'original_price': product.xpath(".//div[@class='p_box_price']/span[2]/text()").get(),
                'User-Agent': response.request.headers['User-Agent']
            }

        # Đối với nhiều trang, thì mình sẽ cho 1 biến, biến này chính là next_page trên trang web
        next_page = response.xpath("//a[@class='nextPage']/@href").get()

        # Giả sử nếu next_page có tồn tại, thì nó sẽ gọi lại chính hàm trên để tiếp tục crawl sang trang tiếp
        # Giả sử trang ko có next_page thì làm thế nào, crawl, click manually, hoặc tìm logic khác
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
            })
