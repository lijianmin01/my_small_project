with open('date.csv','r') as f:
    lines = f.readlines()
    with open('date01.csv','w') as f1:
        for line in lines:
            line_block = list(line.split(" "))
            cnt = line_block[0]
            for i in range(1,len(line_block)-1):
                cnt += ","+line[i]
            cnt+=line_block[-1]
            f1.write(cnt+"\n")


