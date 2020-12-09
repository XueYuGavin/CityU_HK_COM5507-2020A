# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
link=requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20170120&end_date=20201104&fl=headline&fq=sexism&page=5&q=sexism&sort=newest&api-key=VszlmVUfAeh2G8afE6wnuy2wOTUUGGRQ")
result=link.json()
print(result)