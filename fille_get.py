import requests
import json


def make_request():
    s = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    }
    data = {
        'action': 'login',
        'username': 'alevtinanur89@gmail.com',
        'password': 'T9i9w*k$syv~$m*089'
    }
    login_url = 'https://kaspi.kz/merchantcabinet/login'

    s.post(
        url=login_url,
        headers=headers,
        data=data
    )
    return s


def try_api():
    """
    https://kaspi.kz/merchantcabinet/api/order/details/%7Bstatus%7D/210056362
    https://kaspi.kz/merchantcabinet/api/order/search
    {"searchTerm":{"statuses":["ACCEPTED_BY_MERCHANT","SUSPENDED"],"term":null,"orderTab":"DELIVERY","superExpress":false,"returnedToWarehouse":false,"cityId":null,"fromDate":1658685600000,"toDate":1658826819741},"start":0,"count":10}

    """
    s = make_request()
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        'Content-Type': 'application/json',
    }
    product_url = 'https://kaspi.kz/merchantcabinet/api/order/search'
    product_url2 = 'https://kaspi.kz/merchantcabinet/api/order/details/%7Bstatus%7D/210071739'
    request = s.post(
        product_url,
        headers=headers2,
        cookies=s.cookies.get_dict(),
        data=json.dumps({
            "searchTerm": {
                "statuses": ["ACCEPTED_BY_MERCHANT", "SUSPENDED"],
                # "term": null,
                "orderTab": "DELIVERY",
                "superExpress": False,
                "returnedToWarehouse": False,
                # "cityId": null,
                "fromDate": 1658685600000,
                "toDate": 1658826819741
            },
            "start": 0,
            "count": 10})

    )

    request2 = s.post(
        product_url,
        headers=headers2,
        cookies=s.cookies.get_dict(),
        data=json.dumps({
            "searchTerm": {
                "statuses": ["CANCELLED", "COMPLETED", "RETURNED", "RETURN_REQUESTED", "CREDIT_TERMINATION_PROCESS"],
                # "term": null,
                "orderTab": "ARCHIVE",
                "superExpress": False,
                "returnedToWarehouse": False,
                # "cityId": null,
                "fromDate": 1658685600000,
                "toDate": 1658840502146
            },
            "start": 0,
            "count": 10})
    )

    request3 = s.post(
        product_url,
        headers=headers2,
        cookies=s.cookies.get_dict(),
        data=json.dumps({
            "searchTerm": {
                "statuses": ["ACCEPTED_BY_MERCHANT", "SUSPENDED"],
                # "term": null,
                "orderTab": "PICKUP",
                "superExpress": False,
                "returnedToWarehouse": False,
                # "cityId": null,
                "fromDate": 1658685600000,
                "toDate": 1658924052966
            },
            "start": 0,
            "count": 10})
    )

    with open('my_product_1.json', 'w', encoding='utf-8') as my_json:
        json.dump(request.json(), my_json, ensure_ascii=False, indent=4)

    with open('my_product_2.json', 'w', encoding='utf-8') as my_json:
        json.dump(request2.json(), my_json, ensure_ascii=False, indent=4)

    with open('my_product_3.json', 'w', encoding='utf-8') as my_json:
        json.dump(request3.json(), my_json, ensure_ascii=False, indent=4)
