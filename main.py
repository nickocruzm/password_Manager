
try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:   # else block is only executed if try block succeeds.
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")