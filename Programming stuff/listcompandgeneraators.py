import timeit

##print(timeit.timeit('1+3', number = 500000))



##input_list = range(100)
##
##def five(num):
##    if num % 5 == 0:
##        return True
##    else:
##        return False
##
##xyz = (i for i in input_list if five(i))
##
##xyz = [i for i in input_list if five(i)]

print(timeit.timeit('''input_list = range(100)

def five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = [i for i in input_list if five(i)]''', number=5000))
      
