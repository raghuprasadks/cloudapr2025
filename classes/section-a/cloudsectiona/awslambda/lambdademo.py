def greeting():
    return "Welcome"

print(greeting())

hellolambda = lambda : "Hello World from lambda"

print(hellolambda())

def add(n1,n2):
    print("regular function")
    return n1+n2

addlambda = lambda n1,n2 : n1+n2
print(addlambda(10,20))
