D = 20
# some cool party-cles!

for frame in range(3):
    newPage()
    for i in range(2000):
        fill(random(), random(), random())
        posX = (width() + D) * random() - D
        posY = (height() + D) * random() - D
        oval(posX, posY, D, D)

saveImage("06.pdf")
saveImage("06.gif")
