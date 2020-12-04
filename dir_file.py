# >>>>>>>> os.mkdir("newdir") : Directory 생성
import os
# os.mkdir("./dir01")

# >>>>>>>> os.getcwd() : 현재위치
print(os.getcwd())

# >>>>>>>> os.chdir(directory) : 디렉토리이동

# os.chdir(os.getcwd()+'/dir01')

# >>>>>>>> os.rmdir('dirname'): Directory 삭제

# os.mkdir("./dir03")
#os.getcwd()
#os.rmdir("./dir01")

# >>>>>>> os.path.exists(file_name): file 또는　directory 유무
print(os.path.exists('./test/hellow.py'))

# >>>>>>> os.remove(file_name): file 또는　directory 유무
os.remove("./hellow.py")
