import time
def net_price(list_price, discount=0,tax=0.5):
    return list_price * (1 - discount) * (1 + tax)

# print(net_price(100))

def count(end,start=0):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
    print("Done!")

count(5,1)
