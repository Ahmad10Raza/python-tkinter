from PIL import Image

# Open the image file
image = Image.open("IMAGES/Bugatti-Chiron.jpg")

# Resize the image
image = image.resize((700, 700))
image.show()
# Save the image to a new file
image.save("resized_image.jpg")
