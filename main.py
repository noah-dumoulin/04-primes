from math import sqrt

#### Fonction secondaire


def isprime(p):

    
premier =True

s=int(sqrt(p))
for i in range (2,s+1):
    reste=p%i
    if reste==0:
        premier=False
        diviseur=i
        m=int(p/i)
        break
if premier ==False:
    return False
else:
    return True

    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici
    prime(19)
    prime(9)
    prime(55)
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
