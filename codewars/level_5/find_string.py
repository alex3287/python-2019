def my_sort(s):

    m = set(s.strip().lower())
    string = sorted(m)
    string = ''.join(string)
    return string


def find_uniq(arr):
    D = {}
    for i in arr:
        t = my_sort(i)
        D.setdefault(t,0)
        D[t] += 1

    return print(min(D.values()))

if __name__ == "__main__":
    s =['aSdfA ','rty','aasdf','asdf']
    print(find_uniq(s))