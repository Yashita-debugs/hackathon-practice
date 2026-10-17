with open("notes.txt","w") as f:
    while True:
        line= input(("Enter a line (or 'done'): "))
        if line =="done":
            break
        f.write(line+"\n")
with open("notes.txt","r") as f:
    lines = f.readlines()

for i,line in enumerate(lines,start=1):
       print(f"{i}. {line.strip()}")
    # print(i,line.strip())    