str= "x-dspam-confidence: 0.8475"

aa=str.find(":")
bb=str[aa+1:]
print(bb)
value=float(bb)
print(bb)
print(value)
