a = ["3", "4", "5", "-", "1", "-", "5", "-", "2", "/"]

b = ""
acumulador = 0

for i in range (0, len(a)):
    if a[i].isdigit():
        b = b + a[i]
    if a[i] == "/":
        break
    else:
        if not a[i+1].isdigit():  
            acumulador += int(b)   
            b = ""

print(acumulador)