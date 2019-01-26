def my_sort(s):
    s = set(s)
    string = (sorted(s.lower()))
    return string

def find_uniq(arr):
    one = my_sort(arr[0].strip())
    two = my_sort(arr[1].strip())
    l = len(one)
    if len(two)<len(one):
        l = len(two)
    l+=1
    if one[:l] == two[:l]:
        for i in arr:
            if my_sort(i)[:l] != one[:l]:
                return i
    return 's'

if __name__ == "__main__":
    s ='aSdfA'
    print(sorted(s.lower()))