
def kew(**new):
    for key,value in new.items():
        print(f"{key} --> {value}")


kew(name="praveen",age="20")
kew(name="praveen")
kew(name="praveen",age="20",college="mit")
