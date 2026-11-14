# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Anas", color="#e666c8")

transform big:
    zoom 8
    nearest True
    xalign 0.5
    yalign 0.5

image bg:
    "chem.jpeg"
    xsize 1920
    ysize 1080
    fit "cover"

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show bg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ugo at big

    # These display lines of dialogue.
    voice "x.mp3"
    e "Hello World"
    voice sustain
    e "I am Anas"
    voice sustain
    e "Done"

    # This ends the game.

    return
