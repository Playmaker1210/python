a = int(input("a"))
b = int(input("b"))

def osszehasonlitas(a,b):
    if(a > b): return 1
    elif(a == b): return 0
    else: return -1
    
print(osszehasonlitas(a,b))