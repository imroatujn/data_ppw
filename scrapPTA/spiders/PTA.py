import scrapy


class Tugas1Spider(scrapy.Spider):
    name = 'PTA'
    allowed_domains = ['pta.trunojoyo.ac.id']
    start_urls = ['https://pta.trunojoyo.ac.id/c_search/byprod/10/'+str(x)+" " for x in range(2,15)]

    def parse(self, response):
        for link in response.css('a.gray.button::attr(href)') :
            yield response.follow(link.get(),callback=self.parse_categories)

    def parse_categories(self, response):
        products = response.css('div#content_journal ul li')
        for product in products:
            yield {
                'Judul' : product.css('div a.title::text').get().strip(),
                'Penulis' : product.css('div div:nth_child(2) span::text').get().strip(),
                'Dosen 1' : product.css('div div:nth_child(3) span::text').get().strip(),
                'Dosen 2' : product.css('div div:nth_child(4) span::text').get().strip(),
                'Abstrak' : product.css('div div:nth_child(2) p::text').get().strip()
            }
