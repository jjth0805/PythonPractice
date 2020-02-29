#Star tree
# using for
for i in range(1, 20, 2):
    print(('*'*i).center(20))
#half tree
for x in range(1, 10):
    print(('*'*x))

#Convert strings to integers
data = "10, 20, 30"
strings = data.split(',')
print(strings)

#if we want integers then?
numbers = list(
    map(int, data.split(','))
)
print(numbers)

#how to concatenate a few strings
#from a list to a single string
data = [
    "This", "is", "my", "message"
    ]
str = " ".join(data)
print(str)

