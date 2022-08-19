import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip): 
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip):
        splited_number = ip.split(".")
        for i in range(len(splited_number)):
            if (int(splited_number[i]) > 255 or int(splited_number[i]) < 0):
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()