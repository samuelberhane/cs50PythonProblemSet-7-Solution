import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    time =  (re.search(r"^([0-9][0-2]?):?([0-5][0-9])? ([A|P]M) to ([0-9][0-2]?):?([0-5][0-9])? ([A|P]M)$",s))
    if time:
        split_time = time.groups()
        if int(split_time[0]) > 12 or int(split_time[3]) > 12:
            raise ValueError  
        else: 
            first_time =  format24(split_time[0],split_time[1],split_time[2])
            second_time = format24(split_time[3],split_time[4],split_time[5])
            return f"{first_time} to {second_time}"
    else: 
        raise ValueError
    
        
def format24(hr,min,mer):
    if mer == "PM":
        if int(hr) == 12:
            hr = 12
        else:
            hr = int(hr) + 12
    if mer == "AM":
        if int(hr) == 12:
            hr = 0
        else:
            hr = int(hr) 
    if hr < 10:
        hr = f"0{hr}"
    if min == None:
        return f"{hr}:00"
    else:
        if int(min) < 10:
            min = f"0{int(min)}"
        return f"{hr}:{min}"
    

if __name__ == "__main__":
    main()