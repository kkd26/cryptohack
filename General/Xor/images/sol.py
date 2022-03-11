from PIL import Image
from PIL import ImageChops

# Open plaintext file with hex
lemur = Image.open('lemur.png')
flag = Image.open('flag.png')

out = ImageChops.add(ImageChops.subtract(lemur, flag), ImageChops.subtract(flag, lemur))

out.save("save.png")
