import os
import sys

arquivos = [s for s in os.listdir(".") if s.endswith("refs")]

refs = {}
artigos = {}


for arq in arquivos:
    f = open(arq)
    lines = f.readlines()
    f.close()
    refs[arq] = []
    for s in lines:
        if len(s) <= 0 or s == "\t\n" or s == " \t\n":
            continue
        try:
            int(s)
        except:
            refs[arq].append(s)
            if artigos.has_key(s):
                artigos[s] += 1
            else:
                artigos[s] = 1


def checkStrings(s1, s2):
    ls1 = s1.split()
    ls2 = s2.split()
    if len(ls2) > len(ls1):
        ls1, ls2 = ls2, ls1
    val = 0.0
    for w in ls1:
        if w in ls2:
            val += 1.0
    val /= len(ls1)
    return val
    
for key in refs.keys():
    other_keys = [k for k in refs.keys() if k != key]
    for s1 in refs[key]:
        for k in other_keys:
            for s2 in refs[k]:
                val = checkStrings(s1,s2)
                if val >= 0.4:
                    print "---"
                    print s1
                    print s2
                    
                    
