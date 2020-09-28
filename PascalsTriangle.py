def f(line, column):

    if(line == column or line == 0 or column == 0):

        return 1

    
    
    if(column == 1 or column == line - 1):

        return line

    
    return f(line - 1, column - 1) + f(line - 1, column)



def trojkat(lineNumber):

    
    il = 1

    
    for i in range(0, lineNumber):

        for j in range(0, il):
            print(f(i, j), end = " ")

        print("\n")
        il += 1



trojkat(10)