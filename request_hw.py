import requests 
import shopify
API_KEY = "276d42e1d3270aed2b15cb804e348c51"
PASSWORD = "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"
headers = {"Accept": "application/json", "Content-Type": "application/json"}
shop_url = "https://"+API_KEY+":"+PASSWORD+"@lilstore666.myshopify.com"
def create_product(shop_url, header):
    payload = {"product": {
  "body_html": "It's the small iPod with a big idea: Video.",
  "created_at": "2012-02-15T15:12:21-05:00",
  "handle": "ipod-nano",
  "id": 632910392,
  "images": [
    {
      "id": 850703190,
      "product_id": 632910392,
      "position": 1,
      "created_at": "2018-01-08T12:34:47-05:00",
      "updated_at": "2018-01-08T12:34:47-05:00",
      "width": 110,
      "height": 140,
      "src": "http://example.com/burton.jpg",
      "variant_ids": [
        {}
      ]
    }
  ],
  "options": {
    "id": 594680422,
    "product_id": 632910392,
    "name": "Color",
    "position": 1,
    "values": [
      "Pink",
      "Red",
      "Green",
      "Black"
    ]
  },
  "product_type": "Cult Products",
  "published_at": "2007-12-31T19:00:00-05:00",
  "published_scope": "global",
  "status": "active",
  "tags": "Emotive, Flash Memory, MP3, Music",
  "template_suffix": "special",
  "title": "IPod Nano - 8GB",
  "updated_at": "2012-08-24T14:01:47-04:00",
  "variants": [
    {
      "barcode": "1234_pink",
      "compare_at_price": None,
      "created_at": "2012-08-24T14:01:47-04:00",
      "fulfillment_service": "manual",
      "grams": 567,
      "weight": 0.2,
      "weight_unit": "kg",
      "id": 808950810,
      "inventory_item_id": 341629,
      "inventory_management": "shopify",
      "inventory_policy": "continue",
      "inventory_quantity": 10,
      "option1": "Pink",
      "position": 1,
      "price": 199.99,
      "product_id": 632910392,
      "requires_shipping": True,
      "sku": "IPOD2008PINK",
      "taxable": True,
      "title": "Pink",
      "updated_at": "2012-08-24T14:01:47-04:00"
    }
  ],
  "vendor": "Apple"
}
}
    endpoints = "/admin/api/2023-01/products.json"
    r = requests.post(shop_url + endpoints, json=payload,  headers=header)
    return r
# r = create_product(shop_url,headers)
def delete_product(url, product_id):
    endpoints = "/admin/api/2023-01/products/" + str(product_id) + ".json"
    r = requests.delete(url + endpoints)
    return r
# r= delete_product(shop_url,8175161278755)
def create_customer(url, header):
    payload = {
                "customer": {
                    "email": "steve.lastnameson@example.com",
                    "first_name": "Steve",
                    "last_name": "Lastnameson",
                    "state": "enabled",
                    "currency": "VND",  
            }
            }
    endpoints = '/admin/api/2023-01/customers.json'
    r = requests.post(url + endpoints, json = payload, headers=header)
    return r
# r = create_customer(shop_url,headers)
def update_price(url, variant_id):

    payload = {
        'variant':
        {
            "barcode": "1234_pink",
            'price': 12345,
        }
            
    }

    endpoints = "/admin/api/2023-01/variants/" + str(variant_id) + ".json"
    r = requests.put(url+endpoints, json=payload)
    return r
# r = update_price(shop_url,44502662021411)
# print(r.json())
def create_order(url,headers):
    payload = {"order":{
        "line_items":[{"variant_id":44502662021411, "quantity":2}],
        "customer": {"id":6845600891171}
    }}
    endpoints = '/admin/api/2022-04/orders.json'
    r = requests.post(url + endpoints, json=payload, headers=headers)
    return r
# r = create_order(shop_url, headers)
def create_image(url, product_id):
    payload = {
            "image": {
                  "position": 1,
                  "product_id": 8175205843235,
                  "variant_ids": [
                    44502662021411
                  ],
                  "src": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png",
                }
            }
    endpoints = '/admin/api/2023-01/products/' + str(product_id) + '/images.json'
    r = requests.post(url + endpoints, json=payload)
    return r
def create_custom_collection(url, headers):
    payload = {"custom_collection":{
        "title":"ipod",
        "collects":[{"product_id": 8175205843235}, {"product_id":  8175206727971}]
    }}
    endpoints = '/admin/api/2023-01/custom_collections.json'
    r = requests.post(url + endpoints, json=payload, headers=headers)
    return r

def create_smart_collection(url, headers):
    payload = {"smart_collection":{
    "title":"ipod2",
    "rules": [{"column":"title", "relation":"starts_with", "condition":"Quan"}]
    }}
    endpoints = '/admin/api/2022-04/smart_collections.json'
    r = requests.post(url + endpoints, json=payload, headers=headers)
    return r
# r  = create_image(shop_url,8175205843235)
# print(r.json)
# r = create_custom_collection(shop_url, headers)
# print(r.json)
def update_customer(url, customer_id):
    payload = {
        "customer_address": {

                "company": "Litgroup",
                "address1": "trg chinh",
                "address2": "56 To Huu",
                "city": "Hanoi",
                # "province": "Quebec",
                "country": "Vietnam",
                "default": True
    }}
    endpoints = '/admin/api/2023-01/customers/' + str(customer_id)+'/addresses.json'
    r = requests.post(url + endpoints, json=payload)
    return r
# r = update_customer(shop_url, 6845600891171)
def update_quantity(url, inventory_item_id, available):
    tracked = {"inventory_item":{"tracked": True}}
    requests.put(url + '/admin/api/2023-01/inventory_items/' + str(inventory_item_id) + '.json', json=tracked)
    endpoints1 = '/admin/api/2022-04/inventory_levels.json?inventory_item_ids=' + str(inventory_item_id) 
    endpoints2 = '/admin/api/2022-04/inventory_levels/set.json'
    inventory_level = requests.get(url + endpoints1)
    # inventory_level.json()['inventory_levels'][0]['location_id']
    print(inventory_level.json())
    payload = {
    "inventory_item_id": str(inventory_item_id),
    "location_id": str(inventory_level.json()['inventory_levels'][0]['location_id']),
    "available": available}
    r = requests.post(url + endpoints2, json=payload)
    return r
r = update_quantity(shop_url,46599086440739,20 )
print(r.json())