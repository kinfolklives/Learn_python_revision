# dump(obj, file, protocol = None, *, fix_imports = True, buffer_callback = None)
# load(file, *, fix_imports = True, encoding = "ASCII", errors = "strict", buffers = None)

import pickle
favorite_color = {"lion": "yellow", "kitty": "red"}
pickle.dump(favorite_color, open("save.pkl", "wb"))
favorite_color_load = pickle.load(open("save.pkl", "rb"))
favorite_color_load

james_item = [sanitize(each_item) for each_item in james]
print(james_item)
james_item[1:3]
pickle.dump(james_item)