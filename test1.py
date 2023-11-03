import easyocr


render = easyocr.Reader(["en"])

result = render.readtext("image1.jpg")

#print(type(result))

text = ""

for result in result:
    text += result[1] + " " 

print(text)