def split(s):
    return [char for char in s]



def marsExploration(s):
    word='SOS'
    length=len(s)
    word_final=word*(length//3)
    count=0
    index=0
    
    word_final_list=split(word_final)
    list_s=split(s)
    
    for i in word_final_list:
        if list_s[index]!=i:
            count+=1
        index+=1
    return count
    
    
s = input()
result = marsExploration(s)
print(result)
