def print_fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return print_fib(num-1) + print_fib(num-2)


for i in range(0, 10):
    print(print_fib(i) )