import csv
import load
import json
from search import check

json_name = "words_list.json"
MaxSize = load.MaxSize(json_name)
words = load.GetList(json_name)

def GetWord(UserStr,MaxSize,words):
    list_size = len(words)
    temp_word = UserStr[0:MaxSize]
    while len(temp_word) > 1:
        if check(temp_word,words,0,list_size-1):
            return temp_word
        else:
            temp_word = temp_word[0:len(temp_word)-1]
    return temp_word


def divide(fileName):
    with open(fileName,"r") as fileobj:
        csvReader = csv.reader(fileobj)
        headers = next(csvReader)
        dividedNotice = []
        NoticeDic = {}
        count = 0
        for row in csvReader:
            notice = row[0]
            # for i in range(0,len(notice)):
            #     print(notice[i])
            #     if notice[i] < u'\u4e00' or notice[i] > u'\u9fa5':
            #         print(notice[i])
            #         notice = notice[0:i]+notice[i+1:]
            notice = notice[0:-11]
            NoticeDic[count] = notice
            count += 1
            dividedwords = []
            while(len(notice)):
                if len(notice) >= MaxSize:
                    word = GetWord(notice, MaxSize, words)
                    dividedwords.append(word)
                    notice = notice[len(word):]
                else:
                    word = GetWord(notice, len(notice), words)
                    dividedwords.append(word)
                    notice = notice[len(word):]
            dividedNotice.append(dividedwords)
        with open("dividedNotice.json","w") as store:
            json.dump(dividedNotice, store)
        with open("NoticeDic.json", "w") as store:
            json.dump(NoticeDic, store)

divide("zjuNotice.csv")
