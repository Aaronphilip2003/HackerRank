def split(s):
    return [char for char in s]


def pangrams(s):
    print(s)
    list_initial=split(s)
    list_final=[]
    
    for i in list_initial:
        if i not in list_final:
            list_final.append(i)
    length=len(list_final)-1
    if length==26:
        return "panagram"
    else:
        return "not panagram"


s = input()
s=s.lower()
result = pangrams(s)
print(result)
