with open("integers.txt","r",encoding="utf-8") as file:
    ListIntegers = file.read()
ListIntegers = (ListIntegers.split(";"))
print(ListIntegers)
def avgFirstThreeDigit(x):
    num = 0
    for i in x:
        num += int(i[0])*100+ int(i[1])*10 + int(i[2])
    num = list(str(num))
    length = len(num)
    result = list("*"*length)
    number = 0
    while length > 0:
        length -= 1
        a = num[number]
        result[length] = a
        number +=1
    #result = int((str(num))[::-1])
    return result

output= avgFirstThreeDigit(ListIntegers)
print(output)


