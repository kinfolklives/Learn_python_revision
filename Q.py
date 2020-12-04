first, second = input("input two numbers: (a,b) ").split(",")
def sum(first, second):
    s = int(first) + int(second)
    return s, first, second # 리턴시　튜플로　값이　출력된다．　（30, '20', '10) >> 30:int , '20':str 
        
print(sum(first, second))