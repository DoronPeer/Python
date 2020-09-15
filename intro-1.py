
hrs = input("enter hours: ")
rate = input('enter rate: ')
pay = float(hrs) * float(rate)
if pay < 100 :
    print('low')
    print('more time')
else :
    print('okay')    
print('Pay', pay)


inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')



hrs = input("enter hours: ")
rate = input('enter rate: ')
try :
    rate = float(rate)
    hrs = float(hrs)
except :
    print('enter valied numbers')
if hrs < 40 :
    pay = hrs * rate
if hrs > 40 :
    pay = ((40 * rate) + ((hrs - 40) * (rate * 1.5)))
   
print(pay)


grd= input('enter grade')
try :
    float(grd)
except :
    print('enter score in range')
if float(grd) >= 0.9:
    print('A')
elif float(grd) >= 0.8:
    print('B')
elif float(grd) >= 0.7:
    print('C')
elif float(grd) >= 0.6:
    print('D')
elif float(grd) < 0.6:
    print('F')



def computepay(h, r):
    if float(h) < 40 :
        p = (h * r)
    else :
        p = ((40 * r) + ((h - 40) * (r * 1.5)))
    return p  
h = input("Enter Hours:")
r = input('Enter Rate: ')
h = float(h)
r = float(r)
p = computepay(h, r)
print("Pay", p)


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
            break
    try :
        num = int(num)
        if largest is None :
            largest = num
        elif num > largest :
            largest = num
        if smallest is None :
            smallest = num
        elif num < smallest :
            smallest = num      
    except:
        print('Invalid input')
print("Maximum is", largest)
print('Minimum is', smallest)


text = "X-DSPAM-Confidence:    0.8475"
cut = text.find('0')
full = text[cut:]
num = float(full)
print(num)


text = "X-DSPAM-Confidence:    0.8475"
cut = text.find(':')
full = text[cut+1:]
full = full.strip()
num = float(full)
print(num)