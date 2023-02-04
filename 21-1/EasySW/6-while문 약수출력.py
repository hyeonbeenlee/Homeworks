n=int(input())
if n==0:
    print("invalid")
divider=1
string=''
while n:
    if n%divider==0:
        string+=str(divider)+' '
    divider+=1
    if divider==n:
        string+=str(divider)+' '
        break

print(string)