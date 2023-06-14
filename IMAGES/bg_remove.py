from rembg import remove
from PIL import Image
input_path='dev2.jpg'
output_path='dev2.png'
input=Image.open(input_path)
output=remove(input)
output.save(output_path)
