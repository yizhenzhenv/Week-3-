# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:41:30 2024

@author: student
"""
 ============#上課講解=========
import random

# 使用者輸入
n = int(input("請輸入要抽取的數字個數 n："))
a = int(input("請輸入範圍的下限 a："))
b = int(input("請輸入範圍的上限 b："))

random_choose_list=[]

while len(random_choose_list)<n:
    x=random.randint(a,b)
    ramdom_choose_list.append(x)

random_choose_list=set(random_choose_list)
random_choose_list=list(random_choose_list)
random_choose_list.sort()
random_choose_list.reverse()

print(random_choose_list)



 ==========#自己練習=========
import random

# 使用者輸入
n = int(input("請輸入要抽取的數字個數 n："))
a = int(input("請輸入範圍的下限 a："))
b = int(input("請輸入範圍的上限 b："))

# 隨機抽取 n 個 a 到 b 之間的數字
random_numbers = random.sample(range(a, b + 1), n)

# 刪除重複的數字並進行排序
random_numbers = sorted(set(random_numbers), reverse=True)

# 顯示結果
print("隨機抽取且去除重複的數字（由大到小排序）：", random_numbers)
