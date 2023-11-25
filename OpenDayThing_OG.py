HYPE = "HYPE AND MEDIA"

newPage(1080, 1920)
delta = 100
fs = 72

Y = height() / 2 + len(HYPE) * delta / 2 - fs / 2

for letter in HYPE:
    fontSize(fs)
    font(choice(installedFonts()))
    text(letter, (width() / 2, Y), align="center")
    translate(0, -delta)
