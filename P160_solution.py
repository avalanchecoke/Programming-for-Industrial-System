# Homework 3
# P160

testcase = int(input())
for _ in range(testcase):
    n = int(input())
    dish_price = [0 for _ in range(n)]
    dish_type = ['' for _ in range(n)]
    for i in range(n):
        dish = input().split()
        dish_price[i] = int(dish[0])
        dish_type[i] = dish[1]
        
    # code here
    Alice_bill = 0
    Bob_bill = 0
    for i in range(n):
        if dish_type[i] == 'Alice':
            Alice_bill += dish_price[i]
        elif dish_type[i] == 'Bob':
            Bob_bill += dish_price[i]
        elif dish_type[i] == 'Share' and dish_price[i]%2 == 0:
            Alice_bill += dish_price[i] // 2
            Bob_bill += dish_price[i] // 2
        elif dish_type[i] == 'Share' and dish_price[i]%2 != 0:
            Alice_bill += dish_price[i] / 2
            Bob_bill += dish_price[i] / 2
    
    # output
    print(Alice_bill, Bob_bill)