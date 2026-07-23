base = open("base.html", "r").read()
levelsbase = open("./levels/base.html", "r").read()
fun = open("fun.html", "r").read()
levellist = open("list.csv", "r").read()
victorlist = open("victors.csv", "r").read()

levelframe = ""

rank = 1
for lvl in levellist.splitlines()[1:]: # efficiency level ENDLESS
    tslvl = fun
    level = lvl.split(",")
    tslvl = tslvl.replace("||id||", level[0])
    tslvl = tslvl.replace("||unoriginalname||", f"#{rank} - {level[1]}")
    tslvl = tslvl.replace("||creatorlist||", level[2])
    tslvl = tslvl.replace("||status||", level[3])
    tslvl = tslvl.replace("||yt_id||", level[4])

    with open(f"./levels/{level[0]}.html", "w") as levelhtml:
        iforgot = levelsbase
        level = lvl.split(",")
        iforgot = iforgot.replace("||id||", level[0])
        iforgot = iforgot.replace("||unoriginalname||", f"#{rank} - {level[1]}")
        iforgot = iforgot.replace("||creatorlist||", level[2])
        iforgot = iforgot.replace("||status||", level[3])
        iforgot = iforgot.replace("||yt_id||", level[4])

        victors = ""
        victornum = 0
        for levle in victorlist.splitlines():
            if levle.split(",")[0] == level[0]:
                for victor in levle.split(",")[1:]:
                    vrank = f"#{victornum}" if victornum > 0 else "Verifier"
                    victors += f"<b style=\"font-size:20px;\">{vrank} - <a href=\"https://www.youtube.com/watch?v={level[4]}\">{victor.split("|")[0]}</a></b><br>"
                    victornum += 1
        
        iforgot = iforgot.replace("||victorlist||", victors)
        levelhtml.write(iforgot)
    
    
    rank += 1
    levelframe += tslvl

final = base
final = final.replace("||levelframe||", levelframe)
open("index.html", "w").write(final)