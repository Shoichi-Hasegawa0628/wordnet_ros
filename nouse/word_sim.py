#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk
nltk.download('omw-1.4')
from nltk.corpus import wordnet as wn

orange = wn.synset('orange.n.01')
print(orange.member_holonyms())




