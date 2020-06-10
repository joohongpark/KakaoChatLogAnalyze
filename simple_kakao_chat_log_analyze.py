#!/usr/bin/python
#coding=utf-8
import re
from collections import Counter
f = open('chat.txt', encoding='utf-8', errors='ignore')
f_dic = open('result.txt','w+')
date = []
comment = []
comment_raw = []
Hour = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for line in f.readlines(): # 채팅 로그를 Foreach 문을 이용해 한 줄씩 읽어들인다.
    try:
        # 정규식 표현을 이용해 시간과 채팅 내용을 분리한다.
        # 예 - 2016Y 11M 7D PM 1:05, profq님 : 안녕
        reged = re.findall('([0-9]{4})Y ([0-9]{1,2})M ([0-9]{1,2})D ([AP]M) ([0-9]{1,2}):([0-9]{1,2}), ([^:]*) : ([^\n]*)',line)[0]

        # 시간에 따라 채팅 올라온 빈도수 분석하여 Hour 리스트에 해당 시간에 +1을 수행한다.
        if (reged[3] == "AM"): # 오전
            if (int(reged[4]) == 12):
                Hour[0] = Hour[0] + 1
            else:
                Hour[int(reged[4])] = Hour[int(reged[4])] + 1
        else: # 오후
            if (int(reged[4]) == 12):
                Hour[12] = Hour[12] + 1
            else:
                Hour[int(reged[4]) + 12] = Hour[int(reged[4]) + 12] + 1

        # 방에서 가장 많이 사용된 단어 찾기 위한 전처리
        ll = reged[7].split(' ')
        for i in ll:
            comment.append(i)
        
    except:
        continue
for hour, cnt in enumerate(Hour):
    print(str(hour + 1) + "시 : " + str(cnt) + "개의 채팅")
dd = Counter(comment).most_common(1000)
for i in dd:
    f_dic.write(str(i[1]) + "회 : " + i[0] + "\n")
