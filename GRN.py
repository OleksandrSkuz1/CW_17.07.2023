
# def GRN_USD(x):
#     print(x*39.5, "UAN")
#
# a = float(input('Введіть кількість доларів: '))
# GRN_USD(a)

def factorial(fac):
    num = 1
    while fac > 1:
        num *= fac
        fac -= 1
    print(num)

a = int(input("n! = "))
factorial(a)
