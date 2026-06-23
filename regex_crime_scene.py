import re

phone_number="6177777777"

pattern=r"^."

value=re.match(pattern,phone_number)

print(value)

# First crime scene found that character do exist

# Now lets go to the second crime scene to found what will be so second crime scene will be  so phone number starts with the digits actually

# pattern2=r"^\d[7]" 
# it means start of the string one digit and character 7
pattern2=r"^[6-9]\d[7]{8}$"

value2=re.findall(pattern2,phone_number)

print(value2)

## now we will check for another pattern

host_names=["BLR-SW-01","MYS-SW-02"]

pattern3=r"^\w{3}-\w{2}-\d[2]$"



for i in host_names:
    value=re.match(pattern3,i)
    if value:
        print("Yes")

# lets start that whether any mail id is found in the crime scene

pattern4="^\w+\@\w+\.\w+$"

email="tarun@@gmail.com"

email_value=re.match(pattern4,email)

print(email_value)


## Lets start with IP address

ip_address="192.168.29.1"

pattern5=r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

ip_pattern=re.match(pattern5,ip_address)

print(ip_pattern)


