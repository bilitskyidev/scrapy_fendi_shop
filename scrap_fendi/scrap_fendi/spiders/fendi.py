import scrapy
from ..items import ScrapFendiItem
from scrapy_redis.spiders import RedisSpider


class FendiSpider(RedisSpider):
    name = "fendi"
    urls_scrapy = [
        'https://www.fendi.com/us/man/new-arrivals?q=:relevance&page=1&preload=true']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'SCHEDULER': "scrapy_redis.scheduler.Scheduler",
        'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter",
        'ITEM_PIPELINES': {
            'scrapy_redis.pipelines.RedisPipeline': 300
        },
    }

    # def make_request_from_url(self, url):
    #     print('************************************')
    #     print(url)
    #     return scrapy.Request(self.urls_scrapy[0])

    def make_request_from_data(self, data):
        url = self.urls_scrapy[0]
        return scrapy.Request(url)

    def parse(self, response):
        posts_link = response.xpath(
            "//div[contains(@class, 'inner')]/figure/a/@href").extract()
        for i in posts_link[:20]:
            yield scrapy.Request('https://www.fendi.com{}'.format(i), callback=self.parse_post)

    def parse_post(self, response):
        fields_item = ScrapFendiItem()
        fields_item['title'] = self._get_title(response)
        fields_item['price'] = self._get_price(response)
        fields_item['image'] = self._get_image(response)
        fields_item['size'] = self._get_size(response)
        fields_item['description'] = self._get_description(response)
        fields_item['color'] = self._get_color(response)
        return fields_item

    @classmethod
    def _get_title(cls, response):
        title = response.xpath(
            "//div[contains(@class, 'product-description')]/h1/text()").extract_first()
        if title:
            return title

    @classmethod
    def _get_price(cls, response):
        price = response.xpath(
            "//div[contains(@class, 'prices js-price-update')]/span/text()").extract_first().strip()
        if price:
            return price

    @classmethod
    def _get_image(cls, response):
        image = response.xpath(
            "//div[contains(@class, 'inner')]/a/img/@src").extract()
        if image:
            return image

    @classmethod
    def _get_size(cls, response):
        size = response.xpath(
            "//select[contains(@id, 'select-size-sidebar')]/option/@data-qualifier-value").extract()
        if size:
            return size

    @classmethod
    def _get_description(cls, response):
        description = response.xpath(
            "//p[contains(@itemprop, 'description')]/text()").extract_first()
        if description:
            return description

    @classmethod
    def _get_color(cls, response):
        color = response.xpath(
            '//meta[@itemprop="color"]/@content').extract_first()
        if color:
            return color
        else:
            description = response.xpath(
                '//meta[@property="og:description"]/@content').extract_first().split()
            if description and 'sunglasses' not in description:
                if description[1] == 'and':
                    color = description[0:3:2]
                else:
                    color = description[0]
            elif 'and' in description:
                color = description[-4:-1:2]
            elif 'ruthenium' in description:
                color = ' '.join(description[:-1])
            else:
                color = description[-2]
            return color
