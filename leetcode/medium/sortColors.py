def sortColors(nums):
    n = len(nums)
    k = 0
    while k < n:
        if nums[k] == 0:
            del nums[k]
            nums.insert(0,0)
        elif nums[k] == 2:
            del nums[k]
            nums.append(2)
            n -= 1
            k -= 1
        k += 1


    print(nums)


if __name__ == '__main__':
    colors = [1,2,0]
    sortColors(colors)