# Task01
def cemi(numbers):
    a = 0
    for x in numbers:
        a += x
    return(a)

print(cemi((8, 2, 3, 0, 7)))


# Task02
def vurma(numbers):
    a = 1
    for x in numbers:
        a *= x
    return(a)

print(vurma((8, 2, 3, -1, 7)))


# Task03
returnDay = {
1: 'Monday',
2: 'Tuesday',
3: 'Wednesday',
4: 'Thursday',
5: 'Friday',
6: 'Saturday',
7: 'Sunday',
}

def days(number):
    try:
        return returnDay[number]
    except:
        return "None"

print(days(7))


# Task04
def LastElement(list):
    for x in list:
        if x == list[7]:      
            return x
        else:
            if x == [-1]:
                return "eror"
    
print(LastElement((1,2,3,4,5,6,7,8,9,10)))


# Task05
def even(list):
    x=[]
    for x in list:
        if x %2 ==0:     
            x.append(x) 
            return x

    
print(even((1,2,3,4,5,6,7,8,9,10)))