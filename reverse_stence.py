def reverse_sentence(sentence):
    stack = []
    reverse_sentence = ""
    
    for word in sentence.split():
        stack.append(word)
        
    while len(stack)> 0:
        reverse_sentence+=stack.pop()+""
        
    return reverse_sentence.strip()

sentence ="Selamat pagi, bagaimana Kabar Anda?"
print(reverse_sentence(sentence))