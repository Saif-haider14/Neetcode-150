strs = ["Hello" , "Saif"]
# For Encoder
encoder = ""
for i in range(len(strs)):
        
            
    encoder += str(len(strs[i]))+"#"+ strs[i] 
    
print(encoder) 
# For Decoder
decoder = []
while encoder:
    index = encoder.index("#")
    length  = int(encoder[:index])
    word = encoder[index+1 :index+1+length]
    decoder.append(word)
    encoder = encoder[index+1+length :]
print(decoder)
    
    