# arga = allows you to pass multiple non-key arugments
# kwargs = allows you to pass multiple keyword-arugments

# * args is a tupple
# **kwargs is a dictionary

def addFunc(*num):
    total = 0
    for arg in num:
        total+=arg
    return total

print(addFunc(1, 2, 3, 4, 5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name('Dr.', 'Spongebob', 'Harold', 'Squarepants')