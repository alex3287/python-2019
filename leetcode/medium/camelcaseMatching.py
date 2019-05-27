# task 1023. Camelcase Matching

def check(test, master):
    for i in test:
        if test.count(i) > master.count(i):
            return False
    return True

def mask(string):
    L = []
    start =0
    for j in range(len(string)):
        if string[j].upper() == string[j]:
            begin = j+1
            break
    else:
        begin = j
    for i in range(begin,len(string)):
        if string[i].upper() == string[i]:
            L.append(string[start:i])
            start = i
    L.append(string[start:])
    return L

def camelMatch(queries, pattern):
    test = mask(pattern)
    result = []
    for i in queries:
        master = mask(i)
        if len(master) != len(test):
            result.append(False)
            continue
        for a, b in zip(test, master):
            if check(a,b) == False:
                result.append(False)
                break
        else:
            result.append(True)
    return result


if __name__ == '__main__':
    queries = ["CompetitiveProgramming","CounterPick","ControlPanel"]
    pattern = "CooP"
    #queries = ["uAxaqlzahfialcezsLfj", "cAqlzyahaslccezssLfj", "AqlezahjarflcezshLfj", "AqlzofahaplcejuzsLfj",
    #"tAqlzahavslcezsLwzfj", "AqlzahalcerrzsLpfonj", "AqlzahalceaczdsosLfj", "eAqlzbxahalcezelsLfj"]
    #pattern = "AqlzahalcezsLfj"
    print(mask(pattern))
    for i in queries:
        print(mask(i))
    print(camelMatch(queries, pattern))