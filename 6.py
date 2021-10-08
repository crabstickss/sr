print("Введите элементы массива")
try:    
    array = [int(x) for x in input().split()]
    delta = int(input("Введите значение delta:"))
except:
    print('Ошибка')
else:
    a = min(array) + delta
    print ("Количество элементов массиве,отличающихся от минимального на delta = " + str(array.count(a)))
