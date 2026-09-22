import pathlib

# Використовуємо абсолютні шляхи (починаються з '/')
password = pathlib.Path('/etc/passwd')
shadow = pathlib.Path('/etc/shadow')

# 1. Перевірка passwd
if password.exists() and password.is_file():
    print("your file has been found")
    print(password.resolve())
    print(password.stat().st_size)
else:
    print("your password file does not exist")

# 2. Перевірка shadow
if shadow.exists() and shadow.is_file():
    try:
        size = shadow.stat().st_size
        print(f"size of shadow: {size}")
        print(shadow.resolve())
    except PermissionError:
        print("You need to have permission to access the file")
else:
    print("Your shadow file does not exist")