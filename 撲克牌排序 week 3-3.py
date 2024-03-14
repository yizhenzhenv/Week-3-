# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:50:10 2024

@author: student
"""
=========#練習========
import random

# 建立一副撲克牌
suits = ['♠', '♥', '♦', '♣']
ranks = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
deck = [rank+suit for suit in suits for rank in ranks]

# 洗牌
random.shuffle(deck)

player_1 = deck[0::4]
player_2 = deck[1::4]
player_3 = deck[2::4]
player_4 = deck[3::4]

player_1.sort()
player_2.sort()
player_3.sort()
player_4.sort()



'''
# 初始化四個玩家的牌堆
player_hands = [[] for _ in range(4)]

# 發牌
for i, card in enumerate(deck):
    player_hands[i % 4].append(card)

# 對每個玩家的牌進行排序
for hand in player_hands:
    hand.sort(key=lambda x: ranks.index(x[0]))

# 顯示每位玩家的牌
for i, hand in enumerate(player_hands):
    print(f"玩家 {i+1} 的牌：", hand)
'''