#Print harshit four times using recursion
def print_name(count):
    if count == 4:
        return
    print("Harshit")
    print_name(count + 1)
print_name(0)