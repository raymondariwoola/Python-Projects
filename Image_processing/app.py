import image
import math


def black_and_white(img):
    # get the height and width of the image
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            p = img.getPixel(col, row)
            # What are the red, blue and green values for p?
            red_value = p.getRed()
            green_value = p.getGreen()
            blue_value = p.getBlue()
            if (red_value + green_value + blue_value)/3 >= 255/2:
                newred = 255
                newgreen = 255
                newblue = 255
            else:
                newred = 0
                newgreen = 0
                newblue = 0

            # set new pixel to new color values.
            newpixel = image.Pixel(newred, newgreen, newblue)

            img.setPixel(col, row, newpixel)
    # then draw the new images

    newwin = image.ImageWin(img.getWidth(), img.getHeight())
    newimg.draw(newwin)
    return newimg


def black_red_blue_green(img):
    # get the height and width of the image
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            p = img.getPixel(col, row)
            # What are the red, blue and green values for p?
            red_value = p.getRed()
            green_value = p.getGreen()
            blue_value = p.getBlue()
            max_color = max(red_value, blue_value, green_value)
            if red_value + green_value + blue_value >= 550:
                newred = 255
                newgreen = 255
                newblue = 255
            elif red_value + green_value + blue_value <= 150:
                newred = 0
                newgreen = 0
                newblue = 0
            elif max_color == red_value:
                newred = 255
                newgreen = 0
                newblue = 0
            elif max_color == green_value:
                newred = 0
                newgreen = 255
                newblue = 0
            else:
                newred = 0
                newgreen = 0
                newblue = 255

            # set new pixel to new color values.
            newpixel = image.Pixel(newred, newgreen, newblue)

            newimg.setPixel(col, row, newpixel)
    # then draw the new images
    newwin = image.ImageWin(width, height)
    newimg.draw(newwin)
    return newimg


def vignette_effect(img):
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            p = img.getPixel(col, row)
            # find the distance to the center
            distance = math.sqrt((col - width/2)**2+(row - height/2)**2)
            scaling_factor = (height - distance)/height
            newred = p.getRed()*scaling_factor
            newgreen = p.getGreen()*scaling_factor
            newblue = p.getBlue()*scaling_factor
            # set new pixel to new color values.
            newpixel = image.Pixel(int(newred), int(newgreen), int(newblue))
            newimg.setPixel(col, row, newpixel)

    newwin = image.ImageWin(width, height)
    newimg.draw(newwin)

    return newimg


def clarendon_effect(img):
    width = img.getWidth()
    height = img.getHeight()
    scaling_factor = 0.3
    newimg = image.EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            p = img.getPixel(col, row)
            # What are the red, blue and green values for p?
            red_value = p.getRed()
            green_value = p.getGreen()
            blue_value = p.getBlue()

            # average those values
            average_value = (red_value + green_value + blue_value)/3

            # if the cell is light, make it lighter
            if average_value >= 170:
                newred = int(255 - (255 - red_value)*scaling_factor)
                newgreen = int(255 - (255 - green_value)*scaling_factor)
                newblue = int(255 - (255 - blue_value)*scaling_factor)
            elif average_value < 90:
                newred = red_value*scaling_factor
                newgreen = green_value*scaling_factor
                newblue = blue_value*scaling_factor
            else:
                newred = red_value
                newgreen = green_value
                newblue = blue_value

            # set new pixel to new color values.
            newpixel = image.Pixel(newred, newgreen, newblue)

            newimg.setPixel(col, row, newpixel)

    newwin = image.ImageWin(width, height)
    newimg.draw(newwin)
    return newimg


def greyscale(img):
    # get the height and width of the image
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            p = img.getPixel(col, row)
            # What are the red, blue and green values for p?
            red_value = p.getRed()
            green_value = p.getGreen()
            blue_value = p.getBlue()

            # average those values to get the grey value
            gray_value = (red_value + green_value + blue_value)/3

            # set new color values to all be our grey value
            newred = gray_value
            newgreen = gray_value
            newblue = gray_value

            # set new pixel to new color values.
            newpixel = image.Pixel(newred, newgreen, newblue)

            newimg.setPixel(col, row, newpixel)
    # then draw the new images
    newwin = image.ImageWin(width, height)
    newimg.draw(newwin)
    return newimg


def rotate_90_deg(img):
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(height, width)  # fresh canvas for rotated image
    for row in range(height):
        for col in range(width):
            p = img.getPixel(col, row)
            newimg.setPixel((height-1) - row, col, p)
    newwin = image.ImageWin(width, height)
    newimg.draw(newwin)
    return newimg


def rotate_multiples_of_90_deg(img, number):
    angle = int(number*90)
    if angle % 90 != 0:
        print("angle must be a multiple of 90 degrees.")
    elif angle % 360 == 0:
        return img
    elif angle % 360 == 90:
        return rotate_90_deg(img)
    elif angle % 360 == 180:
        return rotate_90_deg(rotate_90_deg(img))
    else:
        return rotate_90_deg(rotate_90_deg(rotate_90_deg(img)))


def enlargeXY(img, xscale, yscale):
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(xscale*width, yscale*height)
    win = image.ImageWin(width, height)
    img.draw(win)
    for row in range(int(yscale*height)):
        for col in range(int(xscale*width)):
            p = img.getPixel(int(col/xscale), int(row/yscale))
            newimg.setPixel(col, row, p)
    return newimg


def BW_highContrast(img):
    #get the height and width of the image
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            p = img.getPixel(col, row)
            #What are the red, blue and green values for p?
            red_value = p.getRed()
            green_value = p.getGreen()
            blue_value = p.getBlue()

            # average those values to get the grey value
            gray_value = (red_value + green_value + blue_value)/3

            if gray_value >= 255/2:
                newred = 255
                newgreen = 255
                newblue = 255
            else:
                newred = 0
                newgreen = 0
                newblue = 0

            #set new pixel to new color values.
            newpixel = image.Pixel(newred, newgreen, newblue)

            newimg.setPixel(col, row, newpixel)
    # then draw the new images
    newwin = image.ImageWin(width, height)
    newimg.draw(newwin)
    return newimg


def lighten(img):
    #get the height and width of the image
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            p = img.getPixel(col, row)
            #What are the red, blue and green values for p?
            red_value = p.getRed()
            green_value = p.getGreen()
            blue_value = p.getBlue()

            scaling_factor = .8
            newred = int(255 - (255 - red_value)*scaling_factor)
            newgreen = int(255 - (255 - green_value)*scaling_factor)
            newblue = int(255 - (255 - blue_value)*scaling_factor)

            #set new pixel to new color values.
            newpixel = image.Pixel(newred, newgreen, newblue)

            newimg.setPixel(col, row, newpixel)
    # then draw the new images
    newwin = image.ImageWin(width, height)
    newimg.draw(newwin)
    return newimg


def darken(img):
    #get the height and width of the image
    width = img.getWidth()
    height = img.getHeight()
    newimg = image.EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            p = img.getPixel(col, row)
            #What are the red, blue and green values for p?
            red_value = p.getRed()
            green_value = p.getGreen()
            blue_value = p.getBlue()

            scaling_factor = .8
            newred = red_value*scaling_factor
            newgreen = green_value*scaling_factor
            newblue = blue_value*scaling_factor

            #set new pixel to new color values.
            newpixel = image.Pixel(newred, newgreen, newblue)

            newimg.setPixel(col, row, newpixel)
    # then draw the new images
    newwin = image.ImageWin(width, height)
    newimg.draw(newwin)
    return newimg
