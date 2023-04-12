D = int(input())
A = int(D/365)
D -= A * 365
M = int(D/30)
D -= M * 30
print(f"{A} ano(s)")
print(f"{M} mes(es)")
print(f"{D} dia(s)")