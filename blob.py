#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:37:16 2020

@author: gavin
"""
headline="Who will win Florida? What the polls say about an eternal mystery"
from textblob import TextBlob
blob=TextBlob(headline)
print(blob.sentences[0].sentiment)