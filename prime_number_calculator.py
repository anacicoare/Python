def is_prime(x):
    x = int(x)
    ok = 1
    if x == 1 or x == 0:
        ok = 0
    else:
        for i in range(2,int(x/2)):
            if x % i == 0:
                ok = 0
    if ok == 0:
        print(f"{x} is not prime.")
    else:
        print(f"{x} is prime.")

x = input("Enter a number to check if it is prime: ")
is_prime(x)