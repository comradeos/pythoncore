def richard(): 
    index = 0
    element = 5 
    li = [5,6,1,2,4,0,3] 
    sortedList = sorted(li)

    while(not(element == sortedList[index]) and len(sortedList) > (index:=index + 1)):
        pass

    return index if (index < len(sortedList)) else -1

print(richard())
