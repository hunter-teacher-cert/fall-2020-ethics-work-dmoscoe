# Daniel Moscoe, Sangmin Pak, and Jonathan Swotinsky
# Ethics and Computer Science
# 12/17/20
# Term Project: The Path To A Visually Accessible Web
# Photo Editing Code

# Reference: Python Imaging Library Documentation (https://omz-software.com/pythonista/docs/ios/PIL.html)

#Reference: How Color Vision Works (https://www.youtube.com/watch?v=VUq_Y3sUYO4&feature=emb_logo)

# Reference: Filters Clarify the Digital World for the Color Blind (https://community.windows.com/en-us/stories/color-filter)

# Reference: Types of Color Blindness, National Eye Institute (https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/color-blindness/types-color-blindness)

# Reference: How to Design for Color Blindness (https://medium.theuxblog.com/how-to-design-for-color-blindness-a6f083b08e12)

# Import Python Imaging Library
from PIL import Image


# Black and White Filter:
def blackAndWhite(fileName0, fileName1):

    # Display a message to let the user know the image is being filtered.
    print("Processing filtered image (Black and white)...")

    # Create an image object for the image the user selected to be filtered:
    img = Image.open(fileName0)

    # For each pixel, check the average RGB value.  If the average RGB value is greater than 127, convert the pixel's color to white.  If the average RGB value is less than or equal to 127, convert the pixel's color to black:
    for n in range(img.size[0]):
        for m in range(img.size[1]):
            # Determine the average RGB value of each pixel:
            pixelTuple = img.getpixel((n, m))
            averageRGB = (pixelTuple[0] + pixelTuple[1] + pixelTuple[2]) / 3

            # If the average RGB value is greater than 127, convert the pixel to white:
            if (averageRGB > 127):
                img.putpixel((n, m), (255, 255, 255, 255))

            # If the average RGB value is less than or equal to 127, convert the pixel to black:
            else:
                img.putpixel((n, m), (0, 0, 0, 255))

    # Create a new file for the filtered image using the filename selected by the user:
    img.save(fileName1)

    # Display a message to let the user know the image has been filtered:
    print("Black and white filter complete.\n")


# Grayscale Filter:
def grayScale(fileName0, fileName1):

    # Display a message to let the user know the image is being filtered.
    print("Processing filtered image (Grayscale)...")

    # Create an image object for the image the user selected to be filtered:
    img = Image.open(fileName0)

    # Convert the color of each pixel to a shade of gray by the red, green, and blue values equal to the average RGB value:
    for n in range(img.size[0]):
        for m in range(img.size[1]):
            # Determine the average RGB value of each pixel:
            pixelTuple = img.getpixel((n, m))
            averageRGB = (pixelTuple[0] + pixelTuple[1] + pixelTuple[2]) / 3

            #Convert the average RGB value to an integer:
            averageRGB = round(averageRGB)

            # Convert the color of each pixel to a shade of gray:
            img.putpixel((n, m), (averageRGB, averageRGB, averageRGB, 255))

    # Create a new file for the filtered image using the filename selected by the user:
    img.save(fileName1)

    # Display a message to let the user know the image has been filtered:
    print("Grayscale filter complete.\n")


# Inverted Grayscale Filter:
def invertedGrayScale(fileName0, fileName1):

    # Display a message to let the user know the image is being filtered.
    print("Processing filtered image (Inverted grayscale)...")

    # Create an image object for the image the user selected to be filtered:
    img = Image.open(fileName0)

    # Convert the color of each pixel to a shade of gray by the red, green, and blue values equal to the average RGB value:
    for n in range(img.size[0]):
        for m in range(img.size[1]):
            # Determine the average RGB value of each pixel:
            pixelTuple = img.getpixel((n, m))
            averageRGB = (pixelTuple[0] + pixelTuple[1] + pixelTuple[2]) / 3

            #Convert the average RGB value to an integer:
            averageRGB = round(averageRGB)

            # Convert the color of each pixel to a shade of gray (inverted):
            img.putpixel(
                (n, m),
                (255 - averageRGB, 255 - averageRGB, 255 - averageRGB, 255))

    # Create a new file for the filtered image using the filename selected by the user:
    img.save(fileName1)

    # Display a message to let the user know the image has been filtered:
    print("Inverted grayscale filter complete.\n")


# Filter for Deuteranomaly: Enhance Green Hues:
# Deuteranomaly is one form of red-green color-blindness.
def Deuteranomaly(fileName0, fileName1):

    # Display a message to let the user know the image is being filtered.
    print("Processing filtered image (Deuteranomaly)...")

    # Create an image object for the image the user selected to be filtered:
    img = Image.open(fileName0)

    # For each pixel, compare the green value to the average RGB value.  If the green value is greater than the average RGB value, raise the green value to 255.
    for n in range(img.size[0]):
        for m in range(img.size[1]):
            # Determine the average RGB value of each pixel:
            pixelTuple = img.getpixel((n, m))
            averageRGB = (pixelTuple[0] + pixelTuple[1] + pixelTuple[2]) / 3

            # Determine the green value of each pixel:
            greenValue = pixelTuple[1]

            # If the green value is greater than the average RGB value raise the green value to 255:
            if (greenValue > averageRGB):
                img.putpixel((n, m), (pixelTuple[0], 255, pixelTuple[2], 255))

    # Create a new file for the filtered image using the filename selected by the user:
    img.save(fileName1)

    # Display a message to let the user know the image has been filtered:
    print("Deuteranomaly filter complete.\n")


# Filter for Protanomaly: Enhance Red Hues:
# Protanomaly is another form of red-green color-blindness.
def Protanomaly(fileName0, fileName1):

    # Display a message to let the user know the image is being filtered.
    print("Processing filtered image (Protanomaly)...")

    # Create an image object for the image the user selected to be filtered:
    img = Image.open(fileName0)

    # For each pixel, compare the red value to the average RGB value.  If the red value is greater than the average RGB value, raise the red value to 255.
    for n in range(img.size[0]):
        for m in range(img.size[1]):
            # Determine the average RGB value of each pixel:
            pixelTuple = img.getpixel((n, m))
            averageRGB = (pixelTuple[0] + pixelTuple[1] + pixelTuple[2]) / 3

            # Determine the red value of each pixel:
            redValue = pixelTuple[0]

            # If the red value is greater than the average RGB value raise the red value to 255:
            if (redValue > averageRGB):
                img.putpixel((n, m), (255, pixelTuple[1], pixelTuple[2], 255))

    # Create a new file for the filtered image using the filename selected by the user:
    img.save(fileName1)

    # Display a message to let the user know the image has been filtered:
    print("Protanomaly filter complete.\n")


# Filter for Tritananomaly: Enhance Blue Hues:
# Tritananomaly is a form of blue-yellow color-blindness.
def Tritananomaly(fileName0, fileName1):

    # Display a message to let the user know the image is being filtered.
    print("Processing filtered image (Tritananomaly)...")

    # Create an image object for the image the user selected to be filtered:
    img = Image.open(fileName0)

    # For each pixel, compare the blue value to the average RGB value.  If the blue value is greater than the average RGB value, raise the blue value to 255.
    for n in range(img.size[0]):
        for m in range(img.size[1]):
            # Determine the average RGB value of each pixel:
            pixelTuple = img.getpixel((n, m))
            averageRGB = (pixelTuple[0] + pixelTuple[1] + pixelTuple[2]) / 3

            # Determine the blue value of each pixel:
            blueValue = pixelTuple[0]

            # If the blue value is greater than the average RGB value raise the blue value to 255:
            if (blueValue > averageRGB):
                img.putpixel((n, m), (pixelTuple[0], pixelTuple[1], 255, 255))

    # Create a new file for the filtered image using the filename selected by the user:
    img.save(fileName1)

    # Display a message to let the user know the image has been filtered:
    print("Tritananomaly filter complete.\n")


# Inverse Filter:
def inverseFilter(fileName0, fileName1):

    # Display a message to let the user know the image is being filtered.
    print("Processing filtered image (Inverse filter)...")

    # Create an image object for the image the user selected to be filtered:
    img = Image.open(fileName0)

    # For each pixel, convert the red, green, and blue values to their inverse:
    for n in range(img.size[0]):
        for m in range(img.size[1]):
            # Generate a tuple of RGB values:
            pixelTuple = img.getpixel((n, m))
            #Convert the red, green, and blue values of each pixel to their inverses:
            img.putpixel((n, m), (255 - pixelTuple[0], 255 - pixelTuple[1],
                                  255 - pixelTuple[2], 255))

    # Create a new file for the filtered image using the filename selected by the user:
    img.save(fileName1)

    # Display a message to let the user know the image has been filtered:
    print("Inverse filter complete.\n")


# Contrast Filter:
def contrastFilter(fileName0, fileName1):

    # Create an image object for the image the user selected to be filtered:
    img = Image.open(fileName0)

    # Accept a contrast level from the user:
    contrastLevel = input("Contrast filter requires a specific contrast level.  Select a number from 1 to 10 to set the contrast level: ")

    # Generate a list of all acceptable contrast levels:
    contrastLevelList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    # Until the user selects a valid choice, prompt them to select again:
    while (contrastLevel not in contrastLevelList):
        contrastLevel = input(
            "\nThis is not a valid entry.  Please enter a number from 1 to 10 to make your selection: "
        )

    # Display a message to let the user know the image is being filtered.
    print("\nProcessing filtered image (Contrast filter)...")

    # For each pixel, check the red green and blue values.  For all values less than or equal to 127, decrease the value by the contrast level (converted to a percent where 1 = 10% and 10 = 100%) of the difference between 0 and the value.  For all values greater than 127, increase the value by the contrast level (converted to a percent as described above) of the different between the value and 255:

    # Convert contrastLevel to a percent:
    contrastLevel = int(contrastLevel) / 10

    for n in range(img.size[0]):
        for m in range(img.size[1]):
            # Generate a tuple of RGB values:
            pixelTuple = img.getpixel((n, m))
            #Determine the red, green, and blue values:
            redValue = pixelTuple[0]
            greenValue = pixelTuple[1]
            blueValue = pixelTuple[2]

            # If the red value is less than or equal to 127, decrease it by the given percent of the difference between 0 and its value:
            if (redValue <= 127):
                redValue = 127 - contrastLevel * redValue
                #Convert the red value to an integer:
                redValue = round(redValue)
            #If the red value is greater than 127, increase it by the given percent of the difference between its value and 255:
            else:
                redValue = redValue + ((250 - redValue) * contrastLevel)
                #Convert the red value to an integer:
                redValue = round(redValue)

            # If the green value is less than or equal to 127, decrease it by the given percent of the difference between 0 and its value:
            if (greenValue <= 127):
                greenValue = 127 - contrastLevel * greenValue
                #Convert the green value to an integer:
                greenValue = round(greenValue)
            #If the green value is greater than 127, increase it by the given percent of the difference between its value and 255:
            else:
                greenValue = greenValue + ((250 - greenValue) * contrastLevel)
                #Convert the green value to an integer:
                greenValue = round(greenValue)

            # If the blue value is less than or equal to 127, decrease it by the given percent of the difference between 0 and its value:
            if (blueValue <= 127):
                blueValue = 127 - contrastLevel * blueValue
                #Convert the red value to an integer:
                blueValue = round(blueValue)
            #If the blue value is greater than 127, increase it by the given percent of the difference between its value and 255:
            else:
                blueValue = blueValue + ((250 - blueValue) * contrastLevel)
                #Convert the blue value to an integer:
                blueValue = round(blueValue)

            #Write the new RGB values to each pixel:
            img.putpixel((n, m), (redValue, greenValue, blueValue, 255))

    # Create a new file for the filtered image using the filename selected by the user:
    img.save(fileName1)

    # Display a message to let the user know the image has been filtered:
    print("Contrast filter complete.\n")


# Have the user select an image to filter, a filename for their filtered image, and a filter:
def filter():
    global fileName0
    global fileName1

    print("\nSelect one of the following filters:")
    print("1 - Black and White.")
    print("2 - Grayscale.")
    print("3 - Inverted Grayscale.")
    print(
        "4 - Deuteranomaly (Red/Green Color Blindness Type 1) - Enhance Green Hues."
    )
    print(
        "5 - Protanomaly (Red/Green Color Blindness Type 2) - Enhance Red Hues."
    )
    print(
        "6 - Tritananomaly (Blue/Yellow Color Blindness) - Enhance Blue Hues.")
    print("7 - Inverse Filter.")
    print("8 - Contrast Filter.")
    print("9 - Run all filters.\n")

    # Accept a filter choice from the user:
    filterChoice = input("Enter a number from 1 to 9 to make your selection: ")
    print()

    # Until the user selects a valid choice, prompt them to select again:
    while (filterChoice != "1" and filterChoice != "2" and filterChoice != "3"
           and filterChoice != "4" and filterChoice != "5"
           and filterChoice != "6" and filterChoice != "7"
           and filterChoice != "8" and filterChoice != "9"):
        filterChoice = input(
            "This is not a valid entry.  Please enter a number from 1 to 9 to make your selection: "
        )
        print()

    # If the user selects 1, run blackandWhite():
    if (filterChoice == "1"):
        blackAndWhite(fileName0, fileName1 + "-blackAndWhite.jpg")
        print("Your filtered image is ready to view!")

    # If the user selects 2, run grayScale():
    elif (filterChoice == "2"):
        grayScale(fileName0, fileName1 + "-grayScale.jpg")
        print("Your filtered image is ready to view!")

    # If the user selects 3, run InvertedGrayScale():
    elif (filterChoice == "3"):
        invertedGrayScale(fileName0, fileName1 + "-invertedGrayScale.jpg")
        print("Your filtered image is ready to view!")

    # If the user selects 4, run Deuteranomaly():
    elif (filterChoice == "4"):
        Deuteranomaly(fileName0, fileName1 + "-Deuteranomaly.jpg")
        print("Your filtered image is ready to view!")

    # If the user selects 5, run Protanomaly():
    elif (filterChoice == "5"):
        Protanomaly(fileName0, fileName1 + "-Protanomaly.jpg")
        print("Your filtered image is ready to view!")

    # If the user selects 6, run Trichromacy():
    elif (filterChoice == "6"):
        Tritananomaly(fileName0, fileName1 + "-Tritananomaly.jpg")
        print("Your filtered image is ready to view!")

    # If the user selects 7, run inverseFilter():
    elif (filterChoice == "7"):
        inverseFilter(fileName0, fileName1 + "-Inverse.jpg")
        print("Your filtered image is ready to view!")

    # If the user selects 8, run contrastFilter():
    elif (filterChoice == "8"):
        contrastFilter(fileName0, fileName1 + "-Contrast.jpg")
        print("Your filtered image is ready to view!")

    # Otherwise, run all filter functions:
    else:
        contrastFilter(fileName0, fileName1 + "-Contrast.jpg")
        blackAndWhite(fileName0, fileName1 + "-blackAndWhite.jpg")
        grayScale(fileName0, fileName1 + "-grayScale.jpg")
        invertedGrayScale(fileName0, fileName1 + "-invertedGrayScale.jpg")
        Deuteranomaly(fileName0, fileName1 + "-Deuteranomaly.jpg")
        Protanomaly(fileName0, fileName1 + "-Protanomaly.jpg")
        Tritananomaly(fileName0, fileName1 + "-Tritananomaly.jpg")
        inverseFilter(fileName0, fileName1 + "-inverseFilter.jpg")
        print("Your filtered images are ready to view!")


# Generate a list to store the name of the file the user would like to edit and the updated filename for the filtered image:
fileName0 = input("Enter the filename of the image you would like to filter: ")
fileName1 = input("Enter a new filename for your filtered image: ")

# Run the program:
filter()