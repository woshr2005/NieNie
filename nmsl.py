# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import pandas
def cookie_to_dict(cookie):
    cookie_dict = {}
    items = cookie.split(';')
    for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        cookie_dict[key] = value
    return cookie_dict
cookie = cookie_to_dict("PHPSESSID=o0fpsvd76vmdsuo3ni1rapn7o1; ulang=en_CA; langToolTipShown=1; _ga=GA1.2.413741556.1553897230; _gid=GA1.2.649169878.1553897230; __utmc=107226066; __utmz=107226066.1553897230.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=107226066.|2=Lang=en_CA=1; hubspotutk=cd49250de048d1e6b31b402f16ce583d; __hssrc=1; __zlcmid=rYi7iq165ktHKO; _fbp=fb.1.1553897231890.977690982; ux=117759; __utma=107226066.413741556.1553897230.1553897230.1553907369.2; __utmt=1; __hstc=152335590.cd49250de048d1e6b31b402f16ce583d.1553897231248.1553897231248.1553907369395.2; __hssc=152335590.1.1553907369395; __utmb=107226066.11.10.1553907369; login_token=%7B%22id%22%3A529955%2C%22user%22%3A117759%2C%22token%22%3A%224c180c03d1f34f3357ff7c27eee857a545f419a72688adafa6e777b164de%22%7D")
df = pandas.read_csv('Spec.csv')
print(df)
for i in df['Spec id']:
    url = 'https://atsspec.com/crm/spec/run-drawing-custom'
    payload = {'specId': str(i)}
    r = requests.post(url, cookies=cookie, data = payload)
    print(r.text)