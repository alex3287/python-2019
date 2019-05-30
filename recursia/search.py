def binSearch(A, target):
    if len(A) < 1:
        return False
    if A[0] == target:
        return True
    n = len(A) // 2
    if target < A[n]:
        return binSearch(A[:n+1],target)
    return binSearch(A[n:], target)

