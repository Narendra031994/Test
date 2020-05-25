a = 10
b = 0
if (b ==0):
    raise ZeroDivisionError("cannot be zero")
try :
    print(a/b)
    """
except ZeroDivisionError as e:
    print("change the b")
    """
finally:
    print(" i will do it any time")