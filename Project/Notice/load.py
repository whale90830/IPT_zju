import json

def MaxSize(json_name):

    MaxSize = 0

    with open(json_name) as file_obj:

        words = json.load(file_obj)

    for word in words:

        if len(word) > MaxSize:

            MaxSize = len(word)

    return MaxSize



def GetList(json_name):

    with open(json_name) as file_obj:

        words = json.load(file_obj)

    return words