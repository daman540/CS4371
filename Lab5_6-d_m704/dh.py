# Helper functions

# Write Function 1 power(a,b,p) that returns a^b mod p using Python’s
# pow function. Handle special case if b == 1
def power(a, b, p):
    # <Enter your code here>
    if b == 1:
        return a % p
    
    return int(pow(a, b, p)) # base, exponent, modulus

# Write Function 2 that generates and returns a public key using P,G,
# and a privateKey chosen by the sender
def dh_generatePublicKey(P,G,privateKey):
    # <Enter your code here>
    public_key = int(pow(G, privateKey, P))
    return public_key

# Write Function 3 that generates and returns a private key using the
# publicKey, privateKey and P chosen by the sender
def dh_generateSecretKey(publicKey, privateKey, P):
    # <Enter your code here>
    secret_key = pow(publicKey, privateKey, P)
    return secret_key

# Function checks if numbers P and G in main
# are co prime with each other
def are_coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1

# Main function
def main():
    P = 0; G = 0; x = 0; a = x;
    y = 0; b = 0;
    ka = 0; kb = 0;

    # Both the users will be agreed upon the public keys G and P
    P = 337; # A prime number P is taken
    print("The value of P: ", P);

    G = 3; # Primitive root for P, G is taken
    print("The value of G: ", G);

    # Checks if both are coprime
    print("P and G is", end =" ")
    if(are_coprime(P, G)):
        print("coprime with each other.")
    else:
        print("not coprime, continuing though.")

    # Alice will choose the private key a
    a = 7; # a is the chosen private key
    print("The private key a for Alice:", a);
    # <Enter code here which calls the appropriate function from above
    # to generate public key for Alice>
    alice_public_key = dh_generatePublicKey(P, G, a)


    # Bob will choose the private key b
    b = 11; # b is the chosen private key
    print("The private key b for Bob:", b);

    # <Enter code here which calls the appropriate function from above
    # to generate public key for Bob>
    bob_public_key = dh_generatePublicKey(P, G, b)

    # Generating the secret key after the exchange of keys
    # <Enter code here which calls the appropriate function from above
    # to generate secret keys for both Alice and Bob. Test that these keys
    # match>
    ka = dh_generateSecretKey(alice_public_key, b, P)
    kb = dh_generateSecretKey(bob_public_key, a, P)

    if ka == kb :
        print("Keys match.")
    else:
        print("Keys do not match.")
    print("Secret key for the Alice is:", str(ka));
    print("Secret Key for the Bob is:", str(kb));

if __name__ == '__main__':
    main()