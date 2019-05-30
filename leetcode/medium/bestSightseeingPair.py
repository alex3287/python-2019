# 1014. Best Sightseeing Pair
# A[i] + A[j] + i - j

def maxScoreSightseeingPair(A):
    max_score = 0
    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] + i - j < 1:
                break
            if A[i] + A[j] + i - j > max_score:
                max_score = A[i] + A[j] + i - j
    return max_score
        


if __name__ == '__main__':
    A = [8,1,5,2,6]
    print(maxScoreSightseeingPair(A))