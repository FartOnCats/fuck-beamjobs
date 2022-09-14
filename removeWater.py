MAGICFONT = "/F4 18 0 R" # beamJobs uses this font for their logo, therefore every element that uses this font is a watermark

# solution? find font, cut out object

"""
TO use simple switch test.pdf to the name of your file, will write output to output.pdf

for the curious; how I managed to find which stream to remove.
In pdf streams contain pretty much all the info that matters, so I just went through each object and removed the accociated stream and 
recorded each change until the water mark was removed
"""
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
    segments.append((startpointer,streamhead))
    
    startpointer = streamend


finalbin = b""
for segment in segments:
    finalbin += pdf[segment[0]:segment[1]]
    print(segment[0],segment[1])

with open("output.pdf","wb") as f:
    f.write(finalbin)
