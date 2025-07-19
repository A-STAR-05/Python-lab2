def vowelcounter(sent):
    vowels = 'aeiouAEIOU'
    v_count={'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
 
    for char in sent:
        if char in vowels:
            v_count[char.lower()]+=1
    return v_count
sentence=input('Enter a sentence: ')
print("Total vowel used in you sentence  is:", vowelcounter(sentence),"The sum is ",sum(vowelcounter(sentence).values()))
        
