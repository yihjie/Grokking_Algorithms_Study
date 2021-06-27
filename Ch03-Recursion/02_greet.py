def greet2(name):
    print("how are you, ", name, "?")

def bye():
    print("ok bye!")

def greet(name):
    print("welcome ", name, "!")
    greet2(name)
    print("getting to say goodbye...")
    bye()

greet("maggie")