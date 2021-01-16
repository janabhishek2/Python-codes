# to get input from user use the input method
# input always return string

x = input("x : ")  # arg-label

print(type(x))  # type(object) return typeOf x

y = int(x)+3

print(f"x is {x} y is {y}")
# use type-conv
# int(x)
# float(x)
# bool(x)
# str(x) for converting to string

# falsy
# 0
# ""
# None
# []
# All others are trusy

print(bool(""))  # falsy
print(bool("False"))  # true

# primitive data types in python : stings,numbers,booleans
