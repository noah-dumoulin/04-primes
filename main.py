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
    print(p,"=", diviseur, "x", m, ": False")
else:
    print(p, ": True")

    pass

#### Fonction principale


def main():
    isprime(5)
    isprime(19)
    isprime(21)
    # vos appels à la fonction secondaire ici
    
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
