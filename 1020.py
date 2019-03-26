dias = int(input())

a = dias // 365
dias = dias % 365

m = dias // 30
dias = dias % 30

d = dias // 1

print("%d ano(s)" % a)
print("%d mes(es)" % m)
print("%d dia(s)" % d)
