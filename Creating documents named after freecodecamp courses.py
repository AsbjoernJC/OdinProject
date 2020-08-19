læs = open("D:\\Odinprojectlists\\AA.txt")
l = læs.readlines()

fl = []
for word in l:
    if word == "Not Passed\n" or word == "\n":
        continue
    else:
        word = word.strip()
        fl.append(word)

for word in fl:
    open("D:\\The odin project\\Applied Accessibility\\" + word + ".html", "w")