from PIL import Image

# ASCII characters
# 12 characters for gray scale
ascii_chars = "@#S%?*+;:,. "

# 70 characters for gray scale
#ascii_chars = "@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# Resizing image
def resize_image(image):
    new_width = 200
    new_height = int(new_width * .5)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)

# Converts the image to grayscale
def gray_scale(image):
    return (image.convert("L"))

# Calculate Pixel Brightness from gray scale and convert pixels to 
# corresponding ASCII character  
def pixel_convert(image):
    pixels = image.getdata()
    characters = "".join([ascii_chars[pixel//25] for pixel in pixels])
    return(characters)

def main():
    # Exception handeling for invalid path names
    path = input('Enter a pathname for an image: \n')
    try:
        image = Image.open(path)
    except Exception as e:
        print('The entered pathname is invalid: {}' .format(e))
        return

    new_image = pixel_convert(gray_scale(resize_image(image)))

    # Gets length of new_image characters and seperates the lines to 
    # the correct number of characters per line based on the width
    pixel_count = len(new_image)
    new_width = 200
    new_image = "\n".join([new_image[index: (index + new_width)] for index in range(0, pixel_count, new_width)])

    # Saves the output to a text file
    with open('ascii_image.txt', 'w') as ascii:
        ascii.write(new_image)

main()
