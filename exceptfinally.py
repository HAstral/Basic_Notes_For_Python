def divide(a , b):
    try:
        c=a/b
    except ZeroDivisionError:
        print("Zero Division Error")
    else:
        print(c)
    finally:
        print('This is always exceuted')

divide(100,10)
divide(100,0)