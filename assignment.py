
# Exercise 1
def count_characters(text):
n=str(input())
m=len(n)
print(m)
    pass

# Exercise 2
def remove_spaces(text):
n=input()
l = ""
for c in n:
    if c!=" ":
        l+=c
print(l)
    pass

# Exercise 3
def count_vowels(text):
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
    pass

# Exercise 4
def replace_vowels(text):
n = input()
vowels = "aeiouAEIOU"
l = ""

for c in n:
    if c in vowels:
        l += "*"
    else:
        l += c
print(l)
    pass

# Exercise 5
def count_words(text):
n=input()
m=n.split()
g=len(m)
print(g)
    pass

# Exercise 6
def find_longest_word(text):
n = input()
words = n.split()

longest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

print(longest)
    pass
