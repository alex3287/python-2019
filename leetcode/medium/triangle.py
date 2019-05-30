# 120. Triangle
def min_index_item(array, num):
    if array[num] < array[num + 1]:
        return array[num], num
    return array[num + 1], num + 1

def search_min(array, num):
    if num == 0:
        return min_index_item(array, num)
    if num == len(array)-1:
        return min_index_item(array, num-1)
    item, index = min(min_index_item(array, num-1), min_index_item(array, num))
    return item, index


def minimumTotal(triangle):
    result = triangle[0][0]
    if len(triangle) == 1:
        return result
    item, index = search_min(triangle[1], 0)
    result += item
    for i, array in enumerate(triangle):
        if i < 2:
            continue
        item, index = search_min(array, index)
        result += item
    return result

if __name__ == '__main__':
    A = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    B=[[1]]
    # print(B[0][0])
    print(minimumTotal(A))
