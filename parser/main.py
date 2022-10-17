import json
def main():
    filecontainer = list()
    filedict = {}
    with open('file.txt','r')as file:
        lines = [line.rstrip('\n') for line in file]
        lines = lines[5:]
    for item in lines:
        x = item.split("    ")
        if len(x)==3:
            filedict = {
                'State' :x[0],
                'Postal Abbr': x[1],
                'FIPS Code' : x[2]
            }
            filecontainer.append(filedict)
            filedict = {}
        else:
            sublist1 = x[:3]
            sublist2 = x[3:]
            filedict = {
                'State' :sublist1[0],
                'Postal Abbr': sublist1[1],
                'FIPS Code' : sublist1[2]
            }
            filecontainer.append(filedict)
            filedict ={}
            filedict = {
                'State' :sublist2[0],
                'Postal Abbr': sublist2[1],
                'FIPS Code' : sublist2[2]
            }
            filecontainer.append(filedict)
    with open('parsed.json','w')as file:
        json.dump(filecontainer,file)



if __name__ == "__main__":
    main()