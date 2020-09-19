fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
    count = count + 1
print(count)


fname = input('Enter file name: ')
try :
    fhand = open(fname)
except :
    print('File cannot be open: ', fname)
    quit()
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
        count = count + 1
print(count)


fname = input('Enter file name: ')
try :
    fhand = open(fname)
except :
    print('File cannot be open: ', fname)
    quit()
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)


fname = input('Enter file name: ')
try :
    fhand = open(fname)
except :
    print('File cannot be open: ', fname)
    quit()
count = 0
total = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") :
         continue
    cut = line.find(':')
    full = line[cut+1:]
    full = full.strip()
    num = float(full)
    count = count + num
    total = total + 1

print('Average spam confidence:', count / total)


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])

#mbox-short.txt

fname = input('Enter file name: ')
try :
    fhand = open(fname)
except :
    print('File cannot be open: ', fname)
    quit()
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    email = line.split()
    print(email[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")


#romeo.txt

fname = input("Enter file name: ")
fhand = open(fname)
words = list()
for line in fhand:
    line = line.rstrip()
    line = line.split()
    for w in line:
        if w in words: 
            continue
        else :
            words.append(w)
words.sort()
print(words)



import string

fhand = open('romeoj.txt')

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

for word in counts:
    print(word, counts[word])

#mbox-short.txt
fname = input('Enter file name: ')
try :
    fhand = open(fname)
except :
    print('File cannot be open: ', fname)
    quit()
counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    email = line.split()
    email = email[1]
    counts[email] = counts.get(email,0) + 1
tn = None
num = None
for email, count in counts.items():
    if tn is None or count > num:
        tn = email
        num = count
print(tn, num)


#word sorting function
import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)





name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)


counts = dict()
for line in fhand:
    
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    time = words[5] 
    time = time[0:2]
    counts[time] = counts.get(time,0) + 1
    

hour = list()
for k,v in list(counts.items()):
    hour.append((k,v))

hour.sort()
for k,v in hour:
    print(k,v)