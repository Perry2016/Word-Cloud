# -*- coding: utf-8 -*-
"""
Created on Mon May  2 01:29:05 2022

@author: datap
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May  1 18:05:24 2022

@author: datap
"""

import requests
import re
from bs4 import BeautifulSoup

url_list = ['https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220429_10680663.shtml',
            'https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220428_10675132.shtml',
            'https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220427_10674571.shtml',
            'https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220426_10673973.shtml',
            'https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220425_10673513.shtml',
            'https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220422_10672257.shtml',
            'https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220421_10671430.shtml',
            'https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220420_10670501.shtml',
            'https://www.mfa.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220419_10669711.shtml',
            'https://www.mfa.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220418_10669204.shtml',
            'https://www.mfa.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220415_10668513.shtml',
            'https://www.mfa.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220414_10668000.shtml',
            'https://www.mfa.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220413_10667402.shtml',
            'https://www.mfa.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220412_10667006.shtml',
            # 'https://www.mfa.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220411_10666674.shtml',
            'https://www.mfa.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220408_10665796.shtml',
            'https://www.mfa.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220407_10665432.shtml',
            'https://www.mfa.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220406_10664971.shtml',
            'https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/202204/t20220401_10663203.shtml'
            ]

kv = {'user-agent': 'Mozilla/5.0'}

country_list = ['美国', '中国']

paragraphs = []

df = open('datapro.txt','w')

for url in url_list:
    
    print(url)
    r = requests.get(url, timeout = 30, headers = kv)

    r.raise_for_status()
    r.encoding = r.apparent_encoding

    demo = r.text

    soup = BeautifulSoup(demo, "html.parser")
    
    print(soup.find_all(string = re.compile("美国")))
    
    for x in soup.find_all(string = re.compile('|'.join(country_list))):
        df.write(str(x))
    
    # df.write(paragraphs)
    
    df.write('\n')
    
df.close()
