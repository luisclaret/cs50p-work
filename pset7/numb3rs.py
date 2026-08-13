import re
import sys

def main():
    print(validate(input("IMv4 Address: ")))
    # ip_address = sys.argv[1] # This is the ip address
    

def validate(ip: str) -> bool:
    ip = ip.strip()
    # if re.fullmatch(r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.){3}", ip):
    if re.fullmatch(r"((25[0-5]|2[0-4][0-9]|((1[0-9]|[1-9])?[0-9]))\.){3}(25[0-5]|2[0-4][0-9]|((1[0-9]|[1-9])?[0-9]))", ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
