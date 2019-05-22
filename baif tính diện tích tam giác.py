def s(a,b):
    if a<=0:
        return "khong hop le"
    a=int(input("nhập a:"))
    b=int(input("nhập b:"))
    c=s(a,b)
    print(c)