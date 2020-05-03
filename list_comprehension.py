from re import split

digits = range(0, 10)
for element in digits:
    if element % 2 == 0:
        print(element)

# devided_on_three
devided_on_three = [x for x in range(0, 51) if x % 3 == 0]
print(devided_on_three)

# Print every word in this sentence that has even numbers of letters
line = "Print every word in this sentence that has even numbers of letters"
print([word for word in line.split() if len(word) % 2 == 0])

# list from 0 to 100; for items mulitples 3 show Fizz, for 5 Buzz for bought (3 & 5) FizzBuzz
hundred_list = range(0, 100)
hundred_list_changed = []
for i in hundred_list:
    if i == 0:
        hundred_list_changed.append(i)
    elif i % 3 == 0 and i % 5 == 0:
        hundred_list_changed.append('FizzBuzz')
    elif i % 3 == 0:
        hundred_list_changed.append('Fizz')
    elif i % 5 == 0:
        hundred_list_changed.append('Buzz')
    else:
        hundred_list_changed.append(i)
print(hundred_list_changed)

# Create a list of fist letters of every word with list comprehension
line2 = "Create a list of fist letters of every word with list comprehension"
print([x[0] for x in line2.split()])


# make string 'AbcerdGdffJdnfd' -> 'aBcErDgDfFjDnFd'

# V1
def changer(*args):
    arr_base = []
    arr_right = []
    new_string = ''
    count = 0
    for letter in args[0]:
        arr_base.append(letter)
    for lll in arr_base:
        if count % 2 == 0:
            arr_right.append(lll.lower())
            count += 1
        else:
            arr_right.append(lll.upper())
            count += 1
    for letter in arr_right:
        new_string = new_string + letter
    return new_string


print(changer('AbcerdGdffJdnfd'))

# V2
def changer2(str):
    result = []
    for i,l in enumerate(str):
        if i % 2 == 0:
           result.append(l.lower())
        else:
            result.append(l.upper())
    return "".join(result)

print(changer2('AbcerdGdffJdnfd'))


def count_primes(num):
    if num < 2:
        return 0

    primes = [2]
    x = 3
    while x <= num:
        print(f'iterations with x = {x}')
        for y in range(3, x, 2):
            print(f'in FOR loop y = {y}')
            print(f'in FOR loop x = {x}')
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            print(f'append x = {x}')
            x += 2
    print(primes)
    return len(primes)

print(count_primes(11))

for f in range(3,11,2):
    print(f'range test {f}')

def myfunc2(str):
    result = []
    for i,l in enumerate(str):
        if i % 2 == 0:
           result.append(l.lower())
        else:
            result.append(l.upper())
    return "".join(result)

print(myfunc2('AbcerdGdffJdnfd'))

# radius function
def vol(rad):
    result = 2*3.14*rad
    return result
print(vol(3))

# is the number in the range
# v. 1
def ran_check(num,low,high):
    result = num in range(low,high)
    return result

def multuply (numbers):
    total = numbers[0]
    for x in numbers:
        total *= x
    return total
print(multuply([2,2,3,-4]))

arr = [2, 2, 3, -4]
total = 1
for i in range(len(arr)):
  total *= arr[i]
print(total)



