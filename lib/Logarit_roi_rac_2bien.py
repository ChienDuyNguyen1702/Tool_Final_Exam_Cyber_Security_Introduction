p=int(input("Nhap vao Module: "))
g=int(input("Nhap vao phan tu sinh: "))
g_bandau=g
z=[]
for i in range(p-1):
    z.append(g**i%p)
print (z)
ga=int(input("Nhap vao g^a: "))
gb=int(input("Nhap vao g^b: "))
key=1
for i in range(p-1):
    if(z[i]==ga):
        key*=i
    if(z[i]==gb):
        key*=i
print("DH",g_bandau,"(",ga,",",gb,") = ",g**key%p)