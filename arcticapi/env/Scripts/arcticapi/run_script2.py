import json
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'arcticapi.settings'
import django
django.setup()

from api.models import Category, Product

def main():
    with open('products.json') as json_file:
        data = json.load(json_file)
    cat = []
    products = data['products']
    for prod in products: 
        if prod['category'] in cat:
            pass
        else: 
            cat.append(prod['category'])
            dbcat = Category()
            dbcat.title = prod['category']
            dbcat.save()
    for prod in products:
        dbprod = Product()
        dbprod.category = Category.objects.filter(title=prod['category']).first()
        dbprod.filename = prod['filename']
        dbprod.name = prod['name']
        dbprod.description = prod['description']
        dbprod.price = prod['price']
        dbprod.save()

if __name__ == '__main__':
    main()