#!/home/zrd/anaconda3/bin/python
import os
import sys 

args = sys.argv
path = "."

strings = ["a"] if len(args)<2 else args[1:] # 要包含的字符串
types = ['png', 'jpg', 'jpeg']
names = os.listdir(path)
img_names = list(filter(lambda name: any(t in name for t in types), names))
need_names = list(filter(lambda name: all(s in name for s in strings), img_names))
rate = len(need_names) / len(img_names)
print(f"{rate:.2%}")
