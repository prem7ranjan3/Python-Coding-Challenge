def reverse_string(num):
    pop_hold = []
    for i in range(len(num)):
        hold_item = num.pop()
        pop_hold.append(hold_item)
    return pop_hold


numbers = list(range(1, 5))
print(reverse_string(numbers))
