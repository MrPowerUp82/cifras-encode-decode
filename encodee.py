carac="abcdefghijklmnopqrstuvwxyz"
carac+=carac.upper()
decodee="-"+carac
encodee="-"+carac[::-1] 
entrada=str(input("->")).replace(" ", "--")
result=[] 
for l in entrada: 
    if l in decodee:
        inde=decodee.index(l)
        result.append(encodee[inde])

result=''.join(result).replace('--',' ')
print(result)
input("\nPress any key to exit!\n")
