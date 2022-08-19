import re

def main():
    print(parse(input("HTML: ")))
    

def parse(s):
    if re.search(r"^<iframe(.)*><\/iframe>$",s):
        youtube_url = re.search(r"(http)(s)?:\/\/(www\.)?youtube\.com\/embed\/(\w+)",s)
        if youtube_url:
            splited_url = youtube_url.groups()      
            return f"https://youtu.be/{splited_url[3]}"
        

if __name__ == "__main__":
    main()