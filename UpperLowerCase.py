#Given a string you are requested to determine whether the string should be converted to all uppercae or all lowercase,depending on the count of uppercase and lowercase letter in that string.
def uplo(inp):
    l1=[]
    l2=[]
    for i in range(len(inp)):
        if inp[i]>='A' and inp[i]<='Z':
            l1.append(inp[i])
        else:
            l2.append(inp[i])
    if len(l1)>len(l2):
        a=inp.upper()
    else:
        a=inp.lower()
    return a
inp=input("Enter a String")
print(uplo(inp))


'''Input:Hello
   Output:hello'''
