
numbers = [1,2,3,1]

def containt_duplicate(num):
    hashset = set()

    for i in num:
        if i in hashset:
            return True
        hashset.add(i)
    return False


