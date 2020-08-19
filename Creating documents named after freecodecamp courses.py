læs = open("D:\\Odinprojectlists\\CSS Grid.txt")
l = læs.readlines()

fl = []
for word in l:
    if word == "Not Passed\n" or word == "\n":
        continue
    else:
        word = word.strip()
        fl.append(word)

for word in fl:
    f = open("D:\\The odin project\\CSS Grid\\" + word + ".html", "w")
    f.write("<!--\n\n\n\n\n-->")