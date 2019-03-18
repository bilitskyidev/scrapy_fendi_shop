from .models import *
from celery.task import task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


@task(name='add_scrap_item')
def add_scrap_item(item_list, end=False):
    for item in item_list:
        item_fendi = ItemShop(
            title=item['title'],
            description=item['description'],
            price=item['price']
        )
        item_fendi.save()
        if item['size']:
            for size in item['size']:
                s = Size(name=size)
                s.save()
                item_fendi.size.add(s.id)
        if item['image']:
            for item_image in item['image']:
                i = Image(name=item_image)
                i.save()
                item_fendi.image.add(i.id)
        if item['color']:
            for item_color in item['color']:
                c = Color(name=item_color)
                c.save()
                item_fendi.color.add(c.id)
    if end:
        for item in ItemShop.objects.all():
            item.status = True
            item.save()
