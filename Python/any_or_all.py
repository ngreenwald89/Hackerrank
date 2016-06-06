num_ints = int(input())
ints = input().split()

def my_check(ints):
    return all([int(num)>0 for num in ints]) and any([num == num[::-1] for num in ints])

print(my_check(ints))
    