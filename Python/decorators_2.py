num_people = int(input())
people = []
for i in range(num_people):
	person = input().split()
	people.append(person)
	
def my_sort(func):
	def inner(people):
		changes = -1
		idx = 0
		while changes != 0:
			idx = 0 
			changes = 0
			while idx < len(people) - 1:
				if people[idx][2] > people[idx + 1][2]:
					people[idx], people[idx + 1] = people[idx + 1], people[idx]
					changes += 1
				idx += 1
		return func(people)
	return inner

def find_gender(func):
	def inner(people):
		ret = []
		for person in people:
			if person[3] == 'M':
				ret.append(' '.join(['Mr.', person[0], person[1]]))
			elif person[3] == 'F':
				ret.append(' '.join(['Ms.', person[0], person[1]]))
		return func(ret)
	return inner

@my_sort
@find_gender
def people_print(people):
	[print(person) for person in people]

people_print(people)