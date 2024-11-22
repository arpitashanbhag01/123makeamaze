import turtle as trtl
import random as rand

apple_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)

drawer = trtl.Turtle()
drawer.hideturtle()

letter_list = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
#choose 5 letters randomly for 5 apples
letters = rand.sample(letter_list, 5) 
#what letters have been used
used = [] 
#apple turtles
apples = []
#posititons for the apples to go to when the program runs
positions = [(0, 150), (-100, 150), (100, 150), (-200, 150), (200, 150)]

#draw letter above the apple
def draw_letter(letter, x, y):
    drawer.penup()
    drawer.goto(x, y)
    drawer.color("white")
    drawer.write(letter, font=("Arial", 74, "bold"))

#create and place apple turtles
def draw_apple():
    global apples
    for i in range(len(letters)):
        apple = trtl.Turtle()
        apple.shape(apple_image)
        apple.penup()
        apple.goto(positions[i])
        apple.letter = letters[i]
        apples.append(apple)
        draw_letter(letters[i], positions[i][0], positions[i][1] + 20)

#apple falls to the ground and comesback up again
def apple_fall(active_apple):
    active_apple.goto(active_apple.xcor(), -150)
    active_apple.goto(active_apple.xcor(), 80)

#when a key is pressed to make the corresponding apple fall down
def key_press(key):
    global apples, used
    if key not in used:
        used.append(key)
        for apple in apples:
            if apple.letter == key:
                apple_fall(apple)
                apples.remove(apple)
                break
    #if all letters are pressed on the apples, clear the letters
    if len(used) == len(letters):
        drawer.clear()

draw_apple()
wn.listen()
for key in letters:
    wn.onkeypress(lambda key=key: key_press(key), key)
wn.bgpic("background.gif")  
wn.mainloop()
