def cmp(a,b):
    print(a,b)
    return(a>b)-(a<b)
# false : 0, true: 1
# tuple 비교시，　어느것　하나라도　큰　것이　있다면　true!
 
tuple1, tuple2 = (123, 'xyz', 1), (456, 'abc', 2)
# Error : (123, 'xyz'), ('abc', 456) : 타입이　서로　일치하지　않음
a = cmp(tuple1, tuple2);    # 괄호　다음에　빈칸이　들어가면　에러남
print(a) # -1

a = cmp(tuple2, tuple1)
print(a) # 1

tuple3 = tuple2 + (786,)    # (786,) : , 주의！　
a = cmp(tuple2, tuple3)
print(a) #-1

