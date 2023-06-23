print('Минимальная сумма инвестиций: ')
x=int(input())
print('У Ивана')
Ivan=int(input())
print('У Майкла')
Mike=int(input())
if (Ivan>=x) and (Mike>=x):
    print(2)
elif (Ivan>=x) or (Mike>=x):
    if (Ivan>=x):
        print('Ivan')
    if (Mike>=x):
        print('Mike')
elif (Ivan+Mike>=x) and not(((Ivan>=x) or (Mike>=x))):
        print(1)
else:
    print(0)