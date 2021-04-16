carac="abcdefghijklmnopqrstuvwxyz" 
decodee="-"+carac
encodee="-"+carac[::-1] 
entrada=str(input("->")).replace(" ", "-")
result=[] 
for l in entrada: 
    if l in decodee:
        inde=decodee.index(l)
        result.append(encodee[inde])

result=str(result).replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","").replace("-"," ") 
print(result)
input("press Enter to exit")
