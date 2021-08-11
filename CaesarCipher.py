def caesarCipher(s, k):
    e = ""
    for i in s:
        if i.islower():
            e+= chr((ord(i)-97+k)%26+97)
        elif i.isupper():
            e+= chr((ord(i)-65+k)%26+65)
        else:
            e+= i
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
