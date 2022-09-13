#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import sqlite3

# WordNetデータの内容の確認
## sqlite_masterという表から、nameという列のデータを取得
# conn = sqlite3.connect("wnjpn.db")
# cur = conn.execute("select name from sqlite_master where type='table'")
# for row in cur:
#     print(row)
#
# ## wordという表から、先頭から5件のデータを取得
# cur = conn.execute("select * from word limit 5")
# for row in cur:
#     print(row)

## wordという表のデータ構造を取得する
# cur = conn.execute("PRAGMA TABLE_INFO(word)")
# for row in cur:
#     print(row)

# Wordnetに登録されているデータ数の確認
# cur = conn.execute("select count(*) from word")
# for row in cur:
#     print("Wordnetに登録されているWordDBの単語数：%s" % row[0])


import wordnet_jp
import pprint

## 指定した単語の類義語、概念を取得
word = ["plate", "bowl", "pitcher_base", "banana", "apple", "orange",
        "cracker_box", "pudding_box", "chips_bag", "coffee", "muscat", "fruits_juice",
        "pig_doll", "sheep_doll", "penguin_doll", "airplane_toy", "car_toy",
        "truck_toy", "tooth_paste", "towel", "cup", "treatments", "sponge", "bath_slipper",
        "frog_shaped_sponge", "duck_shaped_sponge"]

# word = 'penguin'

for w in range(len(word)):
    synonym = wordnet_jp.getSynonym(word[w])
    print(word[w])
    pprint.pprint(synonym)