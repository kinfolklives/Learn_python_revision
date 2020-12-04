# enumerate : index + value 로　출력하는　함수　
some_list = ['foo', 'bar', 'baz']
for index, value in enumerate(some_list):
    print('i:{}, v:{}'.format(index, value))
    
# zip() : 동일한　자리끼리　묶어준다　
# ex. a,1 　／　 b, 2 >> 　　　　　a,b ／ 1,2　　로　출력　

print('-'* 10)
seq1 = ['foo', 'bar', 'baz']
seq2 = ['1','2','3']
seq3 = ['apple', 'pear', 'banana']  # try 2개만

for a, b, c in zip(seq1, seq2, seq3):
    print('a:{}, b:{}, c:{}'.format(a,b,c))
    print ('b:{1}, c:{2}, a:{0}'.format(a,b,c))
    print('-'*10)
    

        