læs = open("D:\\Odinprojectlists\\RWDP.txt")
l = læs.readlines()

fl = []
for word in l:
    if word == "Not Passed\n" or word == "\n":
        continue
    else:
        word = word.strip()
        fl.append(word)

for word in fl:
    f = open("D:\\The odin project\\Responsive Web Design Principles\\" + word + ".html", "w")
    f.write("<!--\n\n-->")