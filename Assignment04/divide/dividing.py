import load


from search import check

def GetWord(UserStr,MaxSize,words):

    list_size = len(words)

    temp_word = UserStr[0:MaxSize]

    while len(temp_word) > 1:

        if check(temp_word,words,0,list_size-1):

            return temp_word

        else:

            temp_word = temp_word[0:len(temp_word)-1]

    return temp_word



def show(word):

    if len(word) > 1:

        print(word)

    elif word >= u'\u4e00' and word <= u'\u9fa5':

        print(word)



json_name = "words_list.json"

MaxSize = load.MaxSize(json_name)

words = load.GetList(json_name)

divided_file = input("请输入文件名")


try:

    with open(divided_file) as file_obj:

        for UserStr in file_obj:

            while(len(UserStr)):

                if len(UserStr)>=MaxSize:

                    word = GetWord(UserStr,MaxSize,words)

                    show(word)

                    UserStr = UserStr[len(word):]

                else:

                    word = GetWord(UserStr,len(UserStr),words)

                    show(word)

                    UserStr = UserStr[len(word):]

except FileNotFoundError:

    print("File Not Found")




