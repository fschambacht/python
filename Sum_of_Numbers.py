def get_sum(a,b):
       
    if a > b:
        a, b = b, a
    if a == b:
        print(a)
        
    x = 0
    for i in range(a, b + 1):
        if a == b:
            continue
        else: x = x + i
    print(x) 

a = -1
b = 2

if __name__ == '__main__':
    get_sum(a, b)