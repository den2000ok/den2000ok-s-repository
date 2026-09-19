from contextlib import closing

file_input = input("please enter the file path: ")
try:
    file = open(file_input, "r")
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("permission denied")
except KeyboardInterrupt:
    print("the reading was interrupted, please restart")
finally
    print("ending, The check has been completed.")
