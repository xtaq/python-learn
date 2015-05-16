fw = open("record.txt", "w")
fw.write('tom, 12, 86\n')
fw.write('tli, 12, 86\n')
fw.write('lucy, 12, 86\n')
fw.write('jose, 12, 86\n')
fw.close()

fr = open("record.txt", "r")
content = fr.readlines()
fr.close()

for i in content :
    print i

