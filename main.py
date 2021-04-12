import sys
import re

s = sys.stdin.read()

print('----')
for line in s.split("\n"):
  if line.startswith("say "):
    if '{' in line:
      a=re.findall("\{(.*)\}","{abcd}H")
      b=re.findall("(\{.*\})","{abcd}H")
      for x,y in zip(a,b):
        line=line.replace(y,str(eval(x)))
    print(re.findall('"([^"]*)"',line)[0])
  if line.startswith("def "):
    t=re.findall('"([^"]*)"',line)
    exec(t[0]+"="+t[1])
    exec("print("+t[0]+")")
