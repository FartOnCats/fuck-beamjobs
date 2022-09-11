import re

MAGICFONT = "/F4 18 0 R" # beamJobs uses this font for their logo, therefore every element that uses this font is a watermark

# solution? find font, cut out object


f = open("test.pdf","rb")
pdf = f.read()
f.close()


startpointer = 0
foundFontSig = 1
segments = []
while foundFontSig > 0:
    foundFontSig = pdf.find(b"\x2F\x46\x34\x20\x31\x38\x20\x30",startpointer)
    streamhead = pdf.find(b"stream",foundFontSig)
    streamend = pdf.find(b"endstream",foundFontSig)
    segments.append((startpointer+6,streamhead))
    
    startpointer = streamend


finalbin = b""
for segment in segments:
    finalbin += pdf[segment[0]:segment[1]]
    print(segment[0],segment[1])

with open("output.pdf","wb") as f:
    f.write(finalbin)
