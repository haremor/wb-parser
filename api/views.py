from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

def json_query(base_url, params):
    response = requests.get(base_url, params=params)
    return response.json()

common_params = {
    'appType': 1,
    'couponsGeo': [12, 3, 18, 15, 21],
    'curr': 'rub',
    'dest': [-1029256, -102269, -2162196, -1257786],
    'couponsGeo': [12, 3, 18, 15, 21],
    'emp': 0,
    'kind': 1,
    'lang': 'ru',
    'locale': 'ru',
    'pricemarginCoeff': 1.0,
    'reg': 0,
    'regions': [80, 64, 83, 4, 38, 33, 70, 69, 86, 75, 30, 40, 48, 1, 66, 31, 68, 22, 71],
    'sort': 'newly',
    'spp': 0,
    'subject': '11;147;216;2287;4575'
}

@api_view(['GET'])
def get_products(req):
    catalog_base_url = 'https://catalog.wb.ru/catalog/men_clothes1/catalog'

    catalog_params = {
        'appType': 1,
        'couponsGeo': [12, 3, 18, 15, 21],
        'curr': 'rub',
        'dest': [-1029256, -102269, -2162196, -1257786],
        'couponsGeo': [12, 3, 18, 15, 21],
        'emp': 0,
        'kind': 1,
        'lang': 'ru',
        'locale': 'ru',
        'page': req.GET.get('page', 1),
        'pricemarginCoeff': 1.0,
        'reg': 0,
        'regions': [80, 64, 83, 4, 38, 33, 70, 69, 86, 75, 30, 40, 48, 1, 66, 31, 68, 22, 71],
        'sort': 'newly',
        'spp': 0,
        # 'subject': 177;284;4853,
    }

    products = json_query(catalog_base_url, catalog_params)
    products = products['data']['products']
    return Response(products)

@api_view(['GET'])
def get_total_products(_):
    total_items_base_url = 'https://catalog.wb.ru/catalog/men_clothes1/v4/filters'


    total_products = json_query(total_items_base_url, common_params)
    total_products = total_products['data']['total']

    return Response({'total': total_products, 'pageNum': round(total_products / 100)})

@api_view(['GET'])
def get_filters(_):
    filters_base_url = 'https://catalog.wb.ru/catalog/men_clothes1/v4/filters'

    filters = json_query(filters_base_url, common_params)
    filters = filters['data']

    return Response(filters)