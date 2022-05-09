import scrapy


class NationalSpider(scrapy.Spider):
    name = 'nationaldebt'
    allowed_domains = 'https://worldpopulationreview.com/'
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response):
        countries = response.xpath("//td/a")
        gdpdebts = response.xpath("//td[2]")
        # print(gdpdebts)

        # for country in countries:
        #     name = country.xpath(".//text()").get()
        #     print(name)
        #
        # for gdpdebt in gdpdebts:
        #     debt = gdpdebt.xpath(".//text()").get()
        #     print(debt)
        rows = response.xpath("(//table[@class='jsx-2006211681 table is-striped is-hoverable is-fullwidth tp-table-body is-narrow'])[1]/tbody/tr")
        # print(rows)
        for row in rows:
            name = row.xpath(".//text()").get()
            debt = row.xpath(".//td[2]/text()").get()
            # print(debt)
            yield {
                'name': name,
                'debt': debt
            }