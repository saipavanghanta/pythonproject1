import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Games")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
gussed_states =[]
while len(gussed_states)<50:
   answer_state = screen.textinput(title=f"{len(gussed_states)}/50 States Correct",prompt="next state").title()

   if answer_state in all_states:
       gussed_states.append(answer_state)
       t = turtle.Turtle()
       t.hideturtle()
       t.penup()
       state_data = data[data.state == answer_state]
       t.goto(int(state_data.x.item()), int(state_data.y.item()))
       t.write(answer_state)



screen.exitonclick()