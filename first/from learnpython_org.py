# first lesson

print("Goodbye, World!")

# second lesson

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20


# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# third lesson

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# 4-th lesson

x = object()
y = object()

x_list = [x]*10
y_list = [y]*10
big_list = y_list + x_list

for x in x_list:
    print(x)


print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")



    #5th lesson
data = ("John", "Doe", 53.44)
format_string = "Hello, %s %s. Your current balance is $%s"

print(format_string % data)

# 6th lesson

