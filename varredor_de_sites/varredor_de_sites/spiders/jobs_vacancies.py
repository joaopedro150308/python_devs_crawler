import scrapy

class IndeedPythonSpider(scrapy.Spider):

    # Identidade
    name = 'vacanciesbot'
    # Request
    def start_requests(self):
        urls = ['https://br.indeed.com/jobs?q=python']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        for element in response.xpath("//td[@class='resultContent css-1qwrrf0 eu4oa1w0']"):
            yield print({
                # Titulo
                'Titulo': element.xpath(".//span[@id]/text()").get(),
                # Local
                'Local': element.xpath(".//td[@class='resultContent css-1qwrrf0 eu4oa1w0']//div[@data-testid='text-location']/text()").get(),
                # Empresa
                'Empresa': element.xpath(".//span[@data-testid='company-name']/text()").get(),
                # Link
                'Link': 'https://br.indeed.com' + element.xpath("//a/@href").get()
            })