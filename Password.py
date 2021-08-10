def split(a):
    return [char for char in a]

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    numbers_l=split(numbers)
    lower_case_l=split(lower_case)
    upper_case_l=split(upper_case)
    special_case_l=split(special_characters)
    
    count_N=0
    count_L=0
    count_U=0
    count_S=0
    count_total=0
    count_return=0
    
    for i in password:
        if i in numbers_l:
            count_N+=1
        elif i in lower_case_l:
            count_L+=1
        elif i in upper_case_l:
            count_U+=1
        elif i in special_case_l:
            count_S+=1
    
    count_total=count_N+count_L+count_U+count_S
    
    if count_N==0:
        count_return+=1
    if count_L==0:
        count_return+=1
    if count_U==0:
        count_return+=1
    if count_S==0:
        count_return+=1
    
    if n>=6:
        return count_return
    elif n<6:
        if(password.isdecimal()):
            return count_total
        else:
            return (6-n)
    
    
        
        
            
            
        




n = int(input().strip())

password = input()

answer = minimumNumber(n, password)

print(answer)
