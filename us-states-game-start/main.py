import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("US STATE GAME")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

Value_of_state = data.state.to_list()
guessed_state = []
should_continue = True
while should_continue:
    ask_user = screen.textinput(title=f"{len(guessed_state)}/50",
                                prompt="What's another state's name?")

    if ask_user in Value_of_state:
        guessed_state.append(ask_user)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(data[data.state == ask_user].x),
               int(data[data.state == ask_user].y))
        t.write(ask_user)
    else:
        print("Game Over")
        should_continue = False

screen.exitonclick()
