# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
=======#上課講解=======
transform={}

transform['a']=A
transform['b']=B
transform['c']=C
transform['d']=D
transform['e']=E
transform['f']=F
transform['g']=G
transform['h']=H
transform['i']=I
transform['j']=J
transform['k']=K
transform['l']=L
transform['m']=M
transform['n']=N
transform['o']=O
transform['p']=P
transform['q']=Q
transform['r']=R
transform['s']=S
transform['t']=T
transform['u']=U
transform['v']=V
transform['w']=W
transform['x']=X
transform['y']=Y
transform['z']=Z

input_string=input(':')
input_string=list(input_string)
for i in range(len(input_string)):
    input_string[i]=transform[input_string[i]
                              
output_string=''.join(input_string)
print(':',output_string)



====#自己練習=======
# 建立字典將小寫字母轉換成大寫字母
key_to_value = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D',
    'e': 'E',
    'f': 'F',
    'g': 'G',
    'h': 'H',
    'i': 'I',
    'j': 'J',
    'k': 'K',
    'l': 'L',
    'm': 'M',
    'n': 'N',
    'o': 'O',
    'p': 'P',
    'q': 'Q',
    'r': 'R',
    's': 'S',
    't': 'T',
    'u': 'U',
    'v': 'V',
    'w': 'W',
    'x': 'X',
    'y': 'Y',
    'z': 'Z'
}

# 使用者輸入英文字串
input_string = input("請輸入一個英文字串：")

# 將輸入的字串轉換為小寫後，逐字轉換成大寫字母並存入列表
converted_list = [key_to_value[char] if char.islower() else char for char in input_string]

# 顯示結果
print("轉換後的字串：", ''.join(converted_list))
