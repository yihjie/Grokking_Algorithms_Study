def countdown(i):
    # Base Case
    print(i)
    if i <= 1:
        return
    # Recursive Case
    else:
        countdown(i - 1)

countdown(5)