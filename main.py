import turtle, pandas, os

def find_file(filename):
    # os is imported due to a bug that image is not being detected despite in the directory. This uses absolute path
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    file_path = os.path.join(script_dir, filename)
    
    return file_path
    
def open_file():
    state_file_path = find_file("50_states.csv")
    contents = pandas.read_csv(state_file_path)
    
    return contents

def setup_screen():
    scrn = turtle.Screen()
    scrn.title("U.S. State Game")
    image_path = find_file("blank_states_img.gif")
    scrn.addshape(image_path)
    turtle.shape(image_path)

def create_state_prompt(answered):
    scrn = turtle.Screen()
    
    return scrn.textinput(title=f"{len(answered)}/50 States Correct", prompt="What's another state's name?")

def print_state(state):
    data = open_file()
    
    s = turtle.Turtle()
    s.hideturtle()
    s.penup()
    s.setpos(float(data[data.state == state.title()].x), float(data[data.state == state.title()].y))
    s.write(state)   
    
def check_answer(user_answer, answered_list):
    data = open_file()
    states_list = data.state.to_list()
    
    if user_answer.title() in states_list and user_answer.title() not in answered_list:
        print_state(user_answer.title())
        answered_list.append(user_answer.title())

def main():
    setup_screen()
    correct_states = []
    
    while len(correct_states) < 50:
        answer_state = create_state_prompt(correct_states)
        
        if answer_state.title() == "Exit":
            data = open_file()
            missing_states = []
            
            for state in data.state:
                if state not in correct_states:
                    missing_states.append(state)
            
            missing_states_data = pandas.DataFrame(missing_states)
            missing_states_data.to_csv("missing_states.csv")
            break
        
        check_answer(answer_state, correct_states)
        
    # mainloop() works like exitonclick() but prevents user from exiting from clicking states
    turtle.mainloop()

if __name__ == "__main__":
    main()