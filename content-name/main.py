import sys

if __name__ == "__main__":

    top_popularity = 150
    eligible_content = []

    f = open(r"content-name/out.log")
    line = f.readline()

    while line:
        if "Interest for" in line:
            # print(line.split(" "))
            line = line.split(" ")
            seq = line[8][:-1]
            name = line[14][:-1]

            if int(seq) < top_popularity+1 and name not in eligible_content:
                eligible_content.append(name)
        line = f.readline()
    
    f.close()

    print(eligible_content)
    print(len(eligible_content))

    str = ""
    for i in range(len(eligible_content)):
        str += eligible_content[i]
    
    print(str)