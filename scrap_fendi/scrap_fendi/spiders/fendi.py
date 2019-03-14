
import scrapy
from ..items import ScrapFendiItem


class FendiSpider(scrapy.Spider):
    name = "fendi"
    start_urls = [
        'https://www.fendi.com/us/man/new-arrivals?q=:relevance&page=1&preload=true']
    custom_settings = {
    'DOWNLOAD_DELAY':2,
    }

    def parse(self, response):
        posts_link = response.xpath("//div[contains(@class, 'inner')]/figure/a/@href").extract()
        for i in posts_link:
            yield scrapy.Request('https://www.fendi.com{}'.format(i), callback=self.parse_post)

    def parse_post(self, response):
        fields_item = ScrapFendiItem()
        fields_item['title'] = response.xpath("//div[contains(@class, 'product-description')]/h1/text()").extract_first()
        fields_item['price'] = response.xpath("//div[contains(@class, 'prices js-price-update')]/span/text()").extract_first().strip()            
        fields_item['image'] = response.xpath("//div[contains(@class, 'inner')]/a/img/@src").extract()
        fields_item['size'] = response.xpath("//select[contains(@id, 'select-size-sidebar')]/option/@data-qualifier-value").extract()
        fields_item['description'] = response.xpath("//p[contains(@itemprop, 'description')]/text()").extract_first()
        fields_item['color'] = response.xpath('//meta[@itemprop="color"]/@content').extract_first()
        return fields_item
