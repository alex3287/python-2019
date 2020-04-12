def tickets(people):
    if len(people)<1:
        return 'YES'
    if people[0] > 25:
        return 'NO'
    coints =[people[0]]  
    for i in range(1,len(people)):
        if people[i] == 50:
            if 25 in coints:
                coints.remove(25)
                coints.append(50)
            else:
                return 'NO'
        elif people[i] == 100:
            if 50 in coints and 25 in coints:
                coints.remove(50)
                coints.remove(25)
                coints.append(100)
            elif coints.count(25) > 2:
                coints.remove(25)
                coints.remove(25)
                coints.remove(25)
                coints.append(100)
            else:
                return 'NO'
        elif people[i] == 25:
            coints.append(25)
    return 'YES'
        
            
print(tickets([]))