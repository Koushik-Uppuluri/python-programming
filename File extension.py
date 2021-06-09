filename = input("Input the Filename: ")
f_extns = filename.split(".")
if f_extns[-1]=='py':
    print("python extension")
elif f_extns[-1]=='c':
    print("c extension")
elif f_extns[-1]=='c++':
    print("Cplusplus extension")
elif f_extns[-1]=='java':
    print("java extension")
elif f_extns[-1]=='txt':
    print("text extension")
else:
    print("invalid extension")
