print("Enter a Number(Zähler):")
a=int(input())

print("Enter a Number(Nenner):")
b=int(input())

if a % b==0:
    print(a,"is devisible by",b)

else:
    print(a,"is not devisible buy",b)