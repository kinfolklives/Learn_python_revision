def differenceVars(*v1, **v2):
    print(v1, type(v1))
    print(v2, type(v2))

# * : list , **": dict

# method 1
differenceVars(1,2,3,4,5,6,a=2, b=3, c=5)

# method 2
args_list=[1,2,3,4]
args_dict={'a':10, 'b':20}
differenceVars(*args_list, **args_dict)

