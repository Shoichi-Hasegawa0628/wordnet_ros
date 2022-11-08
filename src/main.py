#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import wordnet as wn
import pprint
# nltk.download('all') # 初回起動時には必ず行う

# WordNet上の類義語を検索
def wordnet_sim_word(word):
    synonyms = []

    for syn in wn.synsets(word):
        for l in syn.lemmas():
            # print(l.name())
            synonyms.append(l.name())

    return list(set(synonyms))

# 上位, 下位概念の出力
def output_hypo_hyper(word):
    print("{}が含まれている現在の概念を表示します".format(word))
    print(wn.synsets(word)[0], wn.synsets(word)[0].definition())

    print("\n")

    print("{}の上位概念を出力します".format(word))
    for x in wn.synsets(word)[0].hypernym_paths()[0]:
        print(x, x.definition())

    print("\n")

    print("{}の下位概念を出力します".format(word))
    a = wn.synsets(word)
    a = a[0]
    types_of_a = a.hyponyms()
    for x in types_of_a:
        print(x, x.definition())

    return


# WordNetに登録されている単語数を出力 (all, 重複なし)
def output_the_number_of_word_all():
    words = []
    lang_list = sorted(wn.langs())
    # print(lang_list)
    for syn in wn.all_synsets():
        # print(syn)
        # for l in syn.lemmas():
        #     words.append(l.name())

        for l in range(len(lang_list)):
            for w_list in syn.lemmas(lang_list[l]):
                words.append(w_list.name())

    print("WordNetに登録されている単語数(all): {}".format(len(list(set(words)))))


# WordNetに登録されている単語数を出力 (en, 重複なし)
def output_the_number_of_word_en():
    words = []
    for syn in wn.all_synsets():
        # print(syn)
        for l in syn.lemmas():
            words.append(l.name())

    print("WordNetに登録されている単語数(en): {}".format(len(list(set(words)))))


# output_hypo_hyper("living")


# words = ["living", "kitchen", "bathroom", "bedroom"]
# for w in range(len(words)):
#     synonym = wordnet_sim_word(words[w])
#     print(words[w])
#     pprint.pprint(synonym)

output_the_number_of_word_all()

# pprint.pprint(wn.synsets('living'))

# lang_list = sorted(wn.langs())
# print(lang_list)


