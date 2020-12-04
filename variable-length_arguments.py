# def function_name([formal_args,]*var_args_tuple):
#     function_suite
#     return [expression]

def print_return_tuple(arg1, *vartuple):
    print("inside arg1 is: ", arg1)
    for var in vartuple:
        print("inside vartuple is: ", var)
        return vartuple
    
print_return_tuple(10,20)
# inside arg1 is:  10　
# 
out_tuple = print_return_tuple(70, 60, 50)
print(out_tuple)
