import math
print("   Module Z*(p)")
print("   D_log(g) (x) = dap an")
p=int(input("Nhap vao Module p: "))
g=int(input("Nhap vao co so g: "))
x=int(input("Nhap vao x: "))
g_bandau=g
z=[]
for i in range(0,p+1):
    z.append(g**i)
#print(z)
for i in range(0,p):
    if(g**i%p==x):
        print("===> D_log(",g,") (",x,") = ",i)