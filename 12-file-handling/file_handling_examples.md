```
with open("hanu.txt","w") as h:
    h.write("this is hanu \n")
    h.write("this is medikonda \n")
```

```
with open("example1.txt", "w") as f:
    f.write("Hello, this is my first file!\n")
    f.write("Python file handling is easy.\n")
    f.write("my name is hanumantharao medikonda.\n")
```

# 3. Read full content of a file
```
with open("hanu.txt","r") as f:
    result = f.read()
    print(result)

```
# 4. Read file line by line using a loop
```
with open("hanu.txt","r") as f:
    for line in f:
        print(line.strip())
```
#  5. Append new text to an existing file
```
with open("hanu.txt", "a") as f:
    f.write("This is hanu medikonda form guntur !\n")
```
# 6. Read and split lines from a file
```
with open("example1.txt", "r") as f:
     data = f.read()
     result1 = data.splitlines()
     print(result1)
```
# 7. Write a list of names into a file
```
list = ["hanu","mahi","suresh","ramesh","ram"]

with open("hanun.txt","w") as f:
    for a in list:
        f.write(a + "\n")
```
# 8. Copy content from one file to another
```
with open("hanun.txt","r") as src, open("ram.txt","w") as dest:
    for line in src:
        dest.write(line)
```
# 9. Delete a file using pathlib

```
from pathlib import Path

file_path = Path("ram.txt")

if file_path.exists():
    file_path.unlink()  # deletes the file
    print("ram.txt deleted successfully!")
else:
    print("File not found!")
```

