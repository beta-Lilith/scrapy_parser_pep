import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        peps = response.css('a.pep.reference.internal::attr(href)').getall()
        for pep in peps:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css('h1.page-title::text').get().split()
        yield PepParseItem({
            'number': pep_title[1],
            'name': ' '.join(pep_title[3:]),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text').get(),
        })
