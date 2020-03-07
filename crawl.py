import os
import json
import time
import glob

import pandas as pd
import requests
from tqdm import trange, tqdm


class DefaultPick:
    def __init__(self, key):
        self.key = key

    def __call__(self, jsonobj):
        return jsonobj[self.key]


class DefaultTransform:
    def __call__(self, jsonobj):
        return jsonobj


class ComposeTransform(DefaultTransform):
    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, jsonobj):
        for transform in self.transforms:
            jsonobj = transform(jsonobj)
        return jsonobj


class NameTransform(DefaultTransform):
    def __call__(self, jsonobj):
        if jsonobj['name'] is not None:
            jsonobj['name'] = jsonobj['name'].strip().replace(' ', '-')
        return jsonobj


class URLTransform:
    URL_PATTERN = "https://shopee.tw/{name}-i.{shopid}.{itemid}"

    def __call__(self, jsonobj):
        jsonobj['link'] = self.URL_PATTERN.format(**jsonobj)
        return jsonobj


if __name__ == '__main__':
    requests_dir = './requests'
    price_start = 300
    price_end = 2000
    price_tick = 50
    items_per_request = 50
    delay_per_request = 0.1   # 0.5 sec
    retry = 5
    url = "https://shopee.tw/api/v2/search_items"
    params = {
        "by": "price",
        "fe_categoryids": "1563",
        "order": "asc",
        "page_type": "search",
        "version": "2",
        "limit": items_per_request,
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.181 Safari/537.36',
    }
    items_counter = 0
    os.makedirs(requests_dir, exist_ok=True)
    with trange(price_start, price_end, price_tick,
                dynamic_ncols=True) as pbar:
        for price in pbar:
            price_min = price
            price_max = price + price_tick
            pbar.set_postfix(price_min=price_min, price_max=price_max)
            params["price_min"] = price_min
            params["price_max"] = price_max
            items_start = 0
            while True:
                params['newest'] = items_start
                for i in range(retry):
                    try:
                        r = requests.get(url, params=params, headers=headers)
                        break
                    except Exception:
                        pass
                if i == retry - 1 or r.status_code != 200:
                    pbar.write(
                        "price=%d, items_start=%d" % (price, items_start))
                    break
                else:
                    r = r.json()
                    if r['items'] is not None and len(r['items']) != 0:
                        path = os.path.join(requests_dir, "{}_{}.json".format(
                            items_counter, items_counter + items_per_request))
                        with open(path, 'w', encoding='utf8') as f:
                            r['price_range'] = [price_min, price_max]
                            json.dump(r, f, ensure_ascii=False)
                        items_counter += items_per_request
                        items_start += items_per_request
                        pbar.set_description(
                            'items_counter: %d' % items_counter)
                        time.sleep(delay_per_request)
                    else:
                        break

    pattern = os.path.join(requests_dir, "*.json")
    transforms = [
        (
            "name",
            DefaultTransform(), DefaultPick('name')),
        (
            "price_max",
            DefaultTransform(), DefaultPick('price_max')),
        (
            "shopid",
            DefaultTransform(), DefaultPick('shopid')),
        (
            "itemid",
            DefaultTransform(), DefaultPick('itemid')),
        (
            "link",
            ComposeTransform([NameTransform(), URLTransform()]),
            DefaultPick('link')),
    ]
    group = {name: [] for name, _, _ in transforms}
    with tqdm(glob.glob(pattern)) as pbar:
        counter = 0
        for path in pbar:
            with open(path, "r") as f:
                r = json.load(f)
                items = r['items']
            if items is not None:
                for jsonobj in items:
                    jsonobj['price_min'] = r['price_range'][0]
                    jsonobj['price_max'] = r['price_range'][1]
                    for name, transform, pick in transforms:
                        group[name].append(pick(transform(jsonobj)))
                    counter += 1
                    pbar.set_description("%d items" % counter)
    df = pd.DataFrame.from_dict(group)
    df.to_csv('group.csv', index=False)
