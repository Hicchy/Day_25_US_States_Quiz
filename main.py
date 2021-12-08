import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)


text = turtle.Turtle()
text.hideturtle()
text.penup()
numCorrect = 0
isOn = True


while isOn:
    answer = screen.textinput(f"Guess the State {numCorrect}/50", "What's another State?:").title()
    data = pandas.read_csv("50_states.csv")
    states = data["state"]
    states.to_list()
    for haydar in states:
        if answer == haydar:
            state = data[data.state == answer]
            stateX = int(state.x)
            stateY = int(state.y)
            text.setposition(stateX, stateY)
            text.write(answer)
            numCorrect += 1
            if numCorrect == 1:
                print("You win!")
                isOn = False
