# Type Casting
## int
```
print(int(10.5))     # 10 → float to int (decimal truncated)
print(int("10"))     # 10 → string to int (only if string contains valid int)
print(int(True))     # 1  → boolean to int (True=1, False=0)
print(int(10 + 20j)) # ❌ Error → cannot convert complex to int
```
## float
```
print(float(10))  # int to float
print(float(10+20j)) # complex to int not possible
print(float(True)) #    -> boolen to to float
print(float("10")) # string to float
```
## complex
```
print(complex(10)) # int to complex
print(complex(True)) # boolen to complex
print(complex("10)) # strin to complex
print(complex("10.5)) # float to complex
print(complex(10,20)) # int to complex
print(complex(True,False)) # boolen to complex
print(complex(10.5,20.5)) # float to complex
```
## boolen
```
print(bool(0.0))
print(bool(10+20J))
print(bool(''))
print(bool("hanu"))
print(bool(" "))
```
## string
```
print(str(10))
print(str(10.5))
print(str(10+20J))