COLOUR_NAMES = {"aliceblue": "#f0f8ff", "black": "#000000", "blue1": "#0000ff", "antiquewhite": "#faebd7",
                "brown": "#a52a2a", "cadetblue": "#5f9ea0", "coral": "ff7f50", "cyan1": "#00ffff"}

for colour in COLOUR_NAMES:
    print("{:12} is".format(colour), COLOUR_NAMES[colour])

colour = input("Enter colour : ").lower()
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ").lower()
