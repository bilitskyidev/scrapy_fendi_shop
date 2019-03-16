from .models import *
from celery.task import task

def item_params(params, model):
    list_params = []
    for i in params:
        if model == 'Size':
            list_params.append(Size(size_name=i))
        elif model == 'Image':
            list_params.append(Image(image_url=i))
        else:
            list_params.append(Color(image_url=i))
    return 



@task(name='add_scrap_item')
def add_scrap_item(item_list):
    for item in item_list:
        item_fendi = ItemShop(
            title=item['title'],
            description=item['description'],
            price=item['price']
        )



