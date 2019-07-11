s =0.01 #起始值
t = 0.01
d = 0
for i in range(1,30):
    d = s*2
    s = d
    t += d

print(t)
print('1')

