læs = open("D:\\Odinprojectlists\\CSS flexbox.txt")
l = læs.readlines()

fl = []
for word in l:
    if word == "Not Passed\n" or word == "\n":
        continue
    else:
        word = word.strip()
        fl.append(word)

for word in fl:
    f = open("D:\\The odin project\\CSS Flexbox\\" + word + ".html", "w")
    f.write("<!--\n\n-->")