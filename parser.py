from os.path import join

raw_log = "USER: admin ; STATUS: LOCKED ; IP: 10.0.0.45 \n"
cleaned_log = raw_log.strip()
tokens = cleaned_log.split( )
Status = tokens[4]
ip = tokens[7]
status_and_ip = f"Your Ip is {ip}, but  Your Status is {Status}"
print(status_and_ip)

