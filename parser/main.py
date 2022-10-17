import json


def main():
    filecontainer = list()
    filedict = {}
    with open('file.txt', 'r')as file:
        lines = [line.rstrip('\n') for line in file]
        lines = lines[5:]
    for item in lines:
        x = item.split("    ")
        if len(x) == 3:
            filecontainer.append({
                'State': x[0],
                'Postal Abbr': x[1],
                'FIPS Code': x[2]
            })
        else:
            i = 0
            for i in range(2):
                filecontainer.append({
                    'State': x[i],
                    'Postal Abbr': x[i+1],
                    'FIPS Code': x[i+2]
                })
                i+=1

    with open('parsed.json', 'w')as file:
        json.dump(filecontainer, file)


if __name__ == "__main__":
    main()
