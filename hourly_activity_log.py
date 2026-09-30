#E-posta Saat Dağılımı ve Zaman Analizi
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    words=line.split()
    if len(words)<5:
        continue
    if words[0]!="From":
        continue
    zaman=words[5]
    tics=zaman.split(":")
    if len(tics)!=3:
        continue
    saat=tics[0]
    counts[saat]=counts.get(saat,0)+1
for key, value in sorted(counts.items()):
    print(key, value)