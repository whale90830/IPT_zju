import json



words = []

with open("wordslist.txt") as file_obj:

    for word in file_obj:

        words.append(word.rstrip())



words.sort()



with open("words_list.json",'w') as store:

    json.dump(words,store)

