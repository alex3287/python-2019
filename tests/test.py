import heapq
def longest_consec(strarr, k):
    if k > 0:
        temp = [len(i) for i in strarr]
        finder = heapq.nlargest(k, temp)
        result = [strarr[temp.index(i)] for i in finder]
        print(result)
    return ''.join(result)

A = ["zone", "abigail", "theta", "form", "libe", "zas"]
print(longest_consec(A,2))

