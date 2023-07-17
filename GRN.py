
# def GRN_USD(x):
#     print(x*39.5, "UAN")
#
# a = float(input('Введіть кількість доларів: '))
# GRN_USD(a)

# def factorial(fac):
#     num = 1
#     while fac > 1:
#         num *= fac
#         fac -= 1
#     print(num)
#
# a = int(input("n! = "))
# factorial(a)

def isPolindrom(word):
    reverse_word = word[::-1]
    print(reverse_word)
    if reverse_word == word:
        return True
    else:
        return False

if __name__ == "__main__":
    value = input("Введіть слово для перевірки(поліндром): ")
    print(isPolindrom(value))



