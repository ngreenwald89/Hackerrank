string = input().strip()

def marker(char):
    if char.islower():
        return ord(char) - 96
    elif char.isupper():
        return ord(char)
    elif int(char) or int(char) == 0:
        if int(char)%2 == 0:
            return ord(char)*5 + 50
        else:
            return ord(char) + 50
    else:
        print('Not picked up')
        print(char)

def my_sort(string):
    L = sorted(string, key=lambda x: marker(x))
    print(*L, sep='')
my_sort(string)


def alternate_sort(string):
    L = sorted(string, key=lambda x: (x.isdigit() and int(x)%2==0, x.isdigit(), x.isupper()))
    print(*L, sep='')