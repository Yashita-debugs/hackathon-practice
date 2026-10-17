with open("notes.txt","w") as f:
    f.write("Hello\n")
    f.write("Second line\n")
try:
    with open("notes.txt","r") as f:
        content =f.read()
        print(content) 

except FileNotFoundError:
        print("File not found. Check the name and try again.")    

    
   