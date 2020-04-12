# 495. Teemo Attacking
from random import randint as rnd

def findPoisonedDuration(timeSeries, duration):
    result = 0
    if len(timeSeries) < 1:
        return result
    for i in range(len(timeSeries)-1):
        if timeSeries[i+1] - timeSeries[i] >= duration:
            result += duration
        else:
            result += timeSeries[i+1] - timeSeries[i]
    result += duration
    return result

if __name__ == '__main__':
    A = [] # 2
    print(findPoisonedDuration(A,100000))