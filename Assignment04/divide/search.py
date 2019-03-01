def check(word,words,left,right):

    while left<=right:

        mid = int((left+right)/2)

        if word == words[mid]:

            return True

        elif word < words[mid]:

            right = mid - 1

        else:

            left = mid + 1

    if left > right:

        return False

    else:

        return True

