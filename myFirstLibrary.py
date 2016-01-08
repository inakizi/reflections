def myFirstFunction():
    print("Inside My First Function!!!")
    try:
        count = 99
    except KeyError:
        count = 0
    return count
