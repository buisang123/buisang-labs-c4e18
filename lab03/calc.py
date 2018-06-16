n = float(input("x = "))
phep_tinh = input("operation(+,-,*,/): ")
m = float(input("y = "))
result = 0
if phep_tinh == "-":
    result = n - m
elif phep_tinh == "+":
    result = n + m
elif phep_tinh == "*":
    result = n*m
elif phep_tinh == "/":
    result = n/m
print("{0} {1} {2} = {3}".format(n,phep_tinh,m,result))
