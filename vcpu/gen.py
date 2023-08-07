ast=open("main.ast", "r")
print(ast.read)
vars = []
newargs = []
ast_lines = ast.readlines()
for line in ast_lines:
    if line != "" and line != " ":
        print(line.split()[1])
        vars.append(line.split()[1])
        print(str(vars))
        for line in ast_lines:
            spv = line.split()
            print(spv)
            sp = str(spv)
            type= spv[0]
            name= spv[1]
            deffedval = spv[2]
            args=spv.pop(3)        
            out= open("output.py", "w")
            out.write("import helper \n")
            if type == "func":
                for arg in args:
                    if(arg not in vars):
                        newargs.append(arg)
                    elif(arg in vars):
                        if name == arg:
                                            newargs.append(arg)
                        print("in vars")
    
                    
                out.write(f'{name}({newargs}) \n')
    else:
        print("empty")