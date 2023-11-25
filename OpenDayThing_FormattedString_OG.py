def randomBuild(word):
    txt = FormattedString()
    for letter in word:
        txt.font(choice(installedFonts()))
        txt.fontSize(160)
        txt.tracking(80)
        txt.fill(0)
        txt.append(letter)
    return(txt)                                                                                                                                                                                                                     

date = ["NOV", "25"]

def pattern():
    fontSize(50)
    fill(.95)
    blendMode("multiply")    
    for i in range(40, width(), 200):
        for j in range(-10, height(), 100):
            font(choice(installedFonts()))
            text(choice(date), (i,j), align = "center")
    blendMode("normal")

for frame in range(12):
    newPage(1080, 1920)
    frameDuration(1/6)
    HYPE = randomBuild("HYPE")
    AND = randomBuild("AND")
    MEDIA = randomBuild("MEDIA")
    OPEN = randomBuild("OPEN")
    DAY = randomBuild("DAY")

    full = [HYPE, AND, MEDIA, OPEN, DAY]

    fill(1)
    rect(0,0, width(), height())
    pattern()

    translate(0, -303)

    for word in range(len(full)):
        text(full[word], (width()/2, height() - (word + 1) * 242), align = "center")