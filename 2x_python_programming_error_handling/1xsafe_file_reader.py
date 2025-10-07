try:
    f = open("data.txt", "w")
    f.write("Python error handling is important.")
    f.close()
    
    f = open("data.txt", "r")
    content = f.read()
    print(content)
    f.close()
    
except FileNotFoundError:
    print("File does not exist!")