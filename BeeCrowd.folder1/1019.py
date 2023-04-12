S =int(input())
M = int(S/60) 
S -= M*60
H = int(M/60)
M -= H*60
print(f"{H}:{M}:{S}")