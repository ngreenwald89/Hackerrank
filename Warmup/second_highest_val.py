lst_len = input()
lst = input().split()
def second_highest_val(lst):
	my_set = set([int(num) for num in lst])
	my_list = list(sorted(my_set))
	print(my_list[-2:-1][0])

second_highest_val(lst)