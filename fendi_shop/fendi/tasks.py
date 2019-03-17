from .models import *
from celery.task import task




@task(name='add_scrap_item')
def add_scrap_item(item_list, end=False):
    for item in item_list:
        item_fendi = ItemShop(
            title=item['title'],
            description=item['description'],
            price=item['price']
        )
        item_fendi.save()
        if len(item_list['size']) != 0:
            for size in item_list['size']:
                item_fendi.size.add(Size.objects.get_or_create(name=size))
        if len(item_list['image']) != 0:
            for image in item_list['size']:
                item_fendi.image.add(Image.objects.get_or_create(name=image))
        if len(item_list['color']) != 0:
            for color in item_list['color']:
                item_fendi.color.add(Color.objects.get_or_create(name=color))

