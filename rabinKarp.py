#code by Group 7 (Khairina Atiqah)

# d is the number of characters in the input alphabet
# pat  -> pattern
# text  -> text
# q    -> A prime number as a modulo
 
def rabinKarpMatching(pat, text, q):
    N = len(text)
    M = len(pat)
    d = 256
    p = 0    # hash value for pattern
    t = 0    # hash value for text
    h = d**(M-1) % q    # base power calculation to find other hash values of text
 
    for i in range(M):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(text[i]))%q # calculate hash value for first substring of text
    
    # substring sliding
    for i in range(N-M+1):
        if p==t: # if hash value of pattern and text are equal, proceed to string matching
            
            # checks characters one by one
            for j in range(M):
                if text[i+j] != pat[j]:
                    break # substring does not match with pattern
                else: j+=1
 
            # if substring matches with pattern
            if j==M:
                print ("Pattern found at index " + str(i))
 
        # calculates hash value of next substring
        if i < N-M:

            # to reduce time complexity:
            # minus previous hash value with leading character value
            # add trailing character value
            t = (d*(t-ord(text[i])*h) + ord(text[i+M]))%q
 
            # t might be negative, add back modulo value to make it positive
            if t < 0:
                t += q
 
text = "algorisfunalgoisgreat"
pat = "fun"
q = 13
rabinKarpMatching(pat,text,q)
