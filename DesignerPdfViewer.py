def designerPdfViewer(h, word):
    height=[]
    highlight=0
    alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    length=len(word)
    max=0
    
    set_word=set(word)
    
    for i in set_word:
        if i in alpha:
            height.append(alpha.index(i))
    
    for i in height:
        if (h[i]>max):
            max=h[i]
            
    highlight=max*length
    
    return highlight
    
    
        
    



h = list(map(int, input().rstrip().split()))

word = input()

result = designerPdfViewer(h, word)

print(result)
