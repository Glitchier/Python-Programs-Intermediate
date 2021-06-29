import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the States Game")
screen.setup(height=750,width=750)

image_name = "India_outline_map.gif"
screen.addshape(image_name)
turtle.shape(image_name)

data = pandas.read_csv("states.csv")
all_states = data.state.to_list()

guessed_state = []

while(len(guessed_state)<29):

    state_ans=screen.textinput(title=f"{len(guessed_state)}/29", prompt="What's the state? or type exit").title()

    if(state_ans=="Exit"):
        states_missed = []
        for state in all_states:
            if state not in guessed_state:
                states_missed.append(state)
        new_data = pandas.DataFrame(states_missed)
        new_data.to_csv("states_to_learn.csv")
        break

    if(state_ans in all_states):
        guessed_state.append(state_ans)
        t = turtle.Turtle()
        t.shape("circle")
        t.hideturtle()
        t.penup()
        state_data = data[data.state==state_ans]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_ans)

screen.mainloop()