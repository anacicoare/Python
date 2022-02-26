final_number=int(input("Until which number do you want to go?  ")) + 1

for number in range(1,final_number):
    div_3=0
    div_5=0
    if number % 3 == 0:
        div_3 = 1
    if number % 5 == 0:
        div_5 = 1
    print_message = 0
    if div_3 == 1 and div_5 == 1:
        print("Fizzbuzz")
    else:
        if div_3 == 1:
         print("Fizz")
        else:
            if div_5 == 1:
                print("Buzz")
            else:
                print(number)


    