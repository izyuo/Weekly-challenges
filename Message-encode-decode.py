def rotate_en(word,k):
    k=k%len(word)  
    if k == 0:
        return word
    w=word[-k:]          
    w_rev=w[::-1]  
    bal=word[:-k]          
    return w_rev+bal

def rotate_de(word,k):
    k=k%len(word)
    if k==0:
        return word
    w=word[k:]
    w_rev=w[::-1]
    bal=word[:k]
    return w_rev+bal

def encode(sentence):
    words=sentence.split()
    encoded_words=[rotate_en(word,i+1) for i,word in enumerate(words)]
    return " ".join(encoded_words)

def decode(encoded):
    words=encoded.split()
    decoded=[rotate_de(word,i+1) for i,word in enumerate(words)]
    return " ".join(decoded)    



sentence=input("Enter a sentence: ").strip()
encod=encode(sentence)
print("Encoded Message:",encod)


decod=decode(encod)
print("Decoded Message:",decod)
