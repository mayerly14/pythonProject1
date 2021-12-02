# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    num= int(input("Introdueix un nombre natural: "))
    while num < 1:
        num=int(input("Error. Vuelve a introducir un valor natural: "))
    i=0
    sum=0
    while sum+i < num:
        sum = sum + i
        print("El número es", i)
        i+= 1
    print("Y la suma total és:",sum)

if __name__ == '__main__':
    main()


