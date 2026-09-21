
# Exercise 1
n=str(input())
m=len(n)
print(m)

# Exercise 2
n=input()
l = ""
for c in n:
    if c!=" ":
        l+=c
print(l)

# Exercise 3
n=input()
count1=0
count2=0
count3=0
count4=0
count5=0
count=0
for c in n:
    if c=="a":
        count1+=1
    elif c=="e":
        count2+=1
    elif c=="i":
        count3+=1
    elif c=="u":
        count4+=1
    elif c=="o":
        count5+=1
count=count1+count2+count3+count4+count5
print(count)

# Exercise 4
n = input()
vowels = "aeiouAEIOU"
l = ""

for c in n:
    if c in vowels:
        l += "*"
    else:
        l += c
print(l)

# Exercise 5
n=input()
m=n.split()
g=len(m)
print(g)

# Exercise 6
n = input()
words = n.split()

longest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

print(longest)
