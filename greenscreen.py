from PIL import Image

# FIRST PART

# # This line opens the image and loads it into a variable called "image_original"
# image_original = Image.open("./beach.jpg")

# # This line attempts to open a new window to display the image.
# # image_original.show()

# print(image_original.size)  # 800, 600
# print(image_original.format)  # jpeg

# pixels_original = image_original.load()

# # 200, 100 are the x, y exes of the pixel in the image
# print(pixels_original[200, 100])  # 160, 178, 214

# # in the () the order is red, gree, blue. It made a horizontal line
# # pixels_original[200, 100] = (255, 0, 255)
# # pixels_original[201, 100] = (255, 0, 255)
# # pixels_original[202, 100] = (255, 0, 255)
# # pixels_original[203, 100] = (255, 0, 255)
# # pixels_original[204, 100] = (255, 0, 255)

# for y in range(100, 500):
#     for x in range(0, 300):
#         (r, g, b) = pixels_original[x, y]
#         new_blue = b + 50
#         pixels_original[x, y] = (r, g, new_blue)


# image_original.show()
# # image_original.save('name of new image.jpg') to save a new image


image_cactus = Image.open('./cactus.jpg')
image_desert = Image.open('./desert.jpg')

# get width and height
width, height = image_cactus.size

# load pixels
pixels_cactus = image_cactus.load()
pixels_desert = image_desert.load()

# create new black image and load pixels
image_new = Image.new("RGB", image_cactus.size)
pixels_new = image_new.load()

for x in range(0, width):
    for y in range(0, height):
        # compare
        cactus_r, cactus_g, cactus_b = pixels_cactus[x, y]
        desert_r, desert_g, desert_b = pixels_desert[x, y]
        if cactus_g >= 174 and (cactus_b <= 64 and cactus_r <= 130):
            pixels_new[x, y] = (desert_r, desert_g, desert_b)
        else:

            pixels_new[x, y] = (cactus_r, cactus_g, cactus_b)


image_new.show()
image_new.save('combineimage.jpg')
