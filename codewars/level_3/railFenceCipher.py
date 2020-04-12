def encode_rail_fence_cipher(string, n):
    step = (n-1)*2
    s = string[::step]
    for i in range(n-2, 0, -1):
        jump = i*2
        k = 0
        start = k * step + (n - i - 1)
        temp = ''
        right = jump + start
        while len(string) > right:
            temp += string[start] + string[start + jump]
            k += 1
            start = k * step + (n - i - 1)
            right += step
        s += temp
    s += string[step//2::step]
    return s
def decode_rail_fence_cipher(string, n):
    g = len(string) // n
    begin = list(string[:g])
    end = list(string[len(string)-g+1:])
    new_string = [[i] for i in string[g:len(string)-g+1:2]]
    t=[]
    for i in range(g+1):
        t.append(string[g:len(string)-g+1:2])
    part = n - 2
    temp = []
    # for i in range(g-1):
    #     temp.append(begin[i])
    #     for j in range(n-2):
    #         temp.append(new_string[j*n+i])
    #     for k in range(n-2):
    #         temp.append(new_string[n+k+1])
    #     temp.append(end[i])
    temp.append(begin[-1])

    return begin, end, new_string



if __name__ == '__main__':
    test = 'Hello, World!'  # Hoo! el,Wrd l l
    test2 = 'WEAREDISCOVEREDFLEEATONCE'
    test3 = 'Hello, World!'
    test_4 = 'H !e,Wdloollr'
    print(encode_rail_fence_cipher(test3, 4))
    print(decode_rail_fence_cipher(test_4, 4))
