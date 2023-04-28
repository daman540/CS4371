def power(a, b, p):
    if (b == 1):
        return a;
    else:
        return pow(a,b,p)
 
def dh_generatePublicKey(P,G,privateKey):
    #Your code for this function (copy from your lab5 submission)
    public_key = int(pow(G, privateKey, P))
    return public_key
    
def dh_generateSecretKey(publicKey, privateKey, P):
    #Your code for this function (copy from your lab5 submission)
    secret_key = pow(publicKey, privateKey, P)
    return secret_key

    

