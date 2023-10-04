I=input
f=set().union
exec(int(I())*'a=[{*I().split()[1:]}for _ in[0]*int(I())];print(max(len(f(*(x for x in a if{u}-x)))for u in f(*a)));')