def printinfo(fname, fage):
    return fname, fage

name, age = printinfo(fage = 50, fname = 'miki')
print(name + "," + str(age))

# printinfo(a,b) 
# return(a,b) 이므로
# name, age = fname, fage  // because of （a,b)