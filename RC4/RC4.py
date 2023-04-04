key = [1,2,3,6]

sched = [i for i in range(256)]

# Generate scheduling
t = [key[i%len(key)] for i in range(256)]

j = 0
for i in range(10):
    j = (j + sched[i] + t[i]) % 10
    sched[i], sched[j] = sched[j], sched[i]

print(sched[:10])
    
# Cipher    
plain = "hanoi university"
len = len(plain)
i = j = 0
k = [i for i in range(len)]
for t in range(len):
    i = (i+1) % 10
    j = (j + sched[i]) % 10
    sched[i], sched[j] = sched[j], sched[i]
    k[t] = sched[(sched[i] + sched[j]) % 10]


print(k)

cipher = ""

for u in range(len):
    x = ord(plain[u])
    cipher += bin(x^k[u])[2:]
    
print("Cipher: ", cipher)    