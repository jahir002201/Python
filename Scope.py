x = 10  # global scope

def func():
    y = 20  # local scope
    print(x)  # Access global x

func()
