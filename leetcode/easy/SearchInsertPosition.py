from random import randint as rnd

def searchInsert(nums, target):
    for i,item in enumerate(nums):
        if target == item:
            return i
        if target < item:
            return i
    return len(nums)

    # l = 0
    # r = len(nums) - 1
    # while l <= r:
    #     index = (l+r) // 2
    #     if target == nums[index]:
    #         break
    #     if target < nums[index]:
    #         r = index - 1
    #     else:
    #         l = index + 1
    # else:
    #     index
    # index - 1 if target < nums[index] else index + 1
    # return index

if __name__ == '__main__':
    A = [rnd(-10,20) for i in range(10)]
    # A[4]=4
    A.sort()
    print(A)
    print(searchInsert(A, 4))
