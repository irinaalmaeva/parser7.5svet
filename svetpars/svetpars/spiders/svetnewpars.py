import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https://www.divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        def parse(self, response):

            svets = response.css('div._Ud0k')
            for svet in svets:
                yield {
                  'name': svet.css('div.oIrcb span::text').get(),
                  'price': svet.css('div.pY3d2 span::text').get(),
                   'url': svet.css('a').attrib['href']
                }

