import random

def display_message(message):
    """Display a welcome message"""
    print(message)
    
    
def get_user_input(user, input_type = str):
    """Ask user for their name"""
    while True:
        try:
            user_input = input(user)
            return input_type(user)
        except ValueError:
            print("Invalid entry, Please enter your name ")

            
    
    
def setting_the_scene():
    """Ask a player to choose a story"""
    setting = {
        1:"forest",
        2:"castle",
        3:"space"
    }
    display_message("Choose your prefer setting")
    for key, value in setting.items():
         display_message(f"{key}. {value.capitalize()}")
            
    select_setting = get_user_input("Enter a number that correlate to your setting choice ", input_type=int) 
    if select_setting in setting:
        display_message("You are in a {setting[select_setting]}.")
        return setting[select_setting]
    else:
        display_message("Invalid setting choice, Please choose a number from 1 to 3")
        return setting_the_scene
    
def character_creation():
    """Asking player to choose a character"""
    character = {
        1:"hero",
        2:"villain"
    }
    display_message("Choose a character")
    for key, value in character:
        display_message(f"{key}. {value.capitalize()}")
        
    select_character = get_user_input("Enter a number that correlate to your character choice", input_type=int)
    
    if select_character in character:
        display_message("You are a {character[select_character]}.")
        return character[select_character]
    else:
        display_message("Invalid selection, Please choose a number from 1 to 2")
        return character_creation


def plot_development():
    """Develop a basic plot with different events or challenges"""
    events = [
        "A cellphone is found inside a sealed Egyptian tomb. What do you do?\n1. Keep it\n2. Ignore It ",
        "A plane takes off with 81 passengers.It lands with 82. What do you do?\n1. Question it\n2. Report to the airline",
        "As a joke, you use your cellphone to dial your own number.Someone pickup. How will you react\n1. Scream\n2. Change your sim",
        "While on a leisurely stroll through the forest,you find strange footprints.Do you follow them?\n1. I will follow them\n2. I will redirect from the path",
        "You briefly go out in the snow and come back inside.When you go out again,your footprint from earlier lead in a different direction. What do you do\n1. Weary\n2. Scream"
    ]
    for event in events:
        display_message(events)
    decision = get_user_input("Enter 1 or 2 to make your decision", input_type=int)
    if decision == 1:
        display_message("You choose to take action")
    elif decision == 2:
        display_message("You choose to proceed")
    else:
        display_message("Invalid decision. Choose 1 or 2 ")
        
def possible_outcome():
    """Variables to represent possible outcomes"""
    outcomes = {
        "happy ending":["You have successful completed your trivia quest and achieved happy ending.Good job", "Congratulation"],
        "tragic ending":["Unluckily your journey took a tragic turn. Better luck next time !"]
        
    }
    closing_outcomes = random.choice(list(outcomes.keys()))
    display_message(outcomes[closing_outcomes][0])
    display_message(outcomes[closing_outcomes][1])
    
    
def write_to_file():
    """Writing and saving to a file by user choice"""  
    story = '''
        "A cellphone is found inside a sealed Egyptian tomb. What do you do?\na. Keep it\nb. Ignore It ",
        "A plane takes off with 81 passengers.It lands with 82. What do you do?\na. Question it\nb. Report to the airline",
        "As a joke, you use your cellphone to dial your own number.Someone pickup. How will you react\na. Scream\nb. Change your sim",
        "While on a leisurely stroll through the forest,you find strange footprints.Do you follow them?\na. I will follow them\nb. I will redirect from the path",
        "You briefly go out in the snow and come back inside.When you go out again,your footprint from earlier lead in a different direction. What do you do\na. Weary\nb. Scream"
    '''

    try:
        write_to = get_user_input("Enter Yes or No to proceed", input_type=str)
        if write_to.isalpha() == 'yes':
                file_name = get_user_input("Enter filename(e.g.,story)", input_type=str)  
        elif file_name.isalpha() == 'story':
                    file_name = get_user_input("Do you want to save into text file:", input_type=str)
        if filename.isalpha() == 'yes':
                         with open('story.txt','w') as filename:
                            filename.write(story)
                            print("Your story has been save to a text file")
    except ValueError:
        print("Invalid input, try again")
        return write_to_file
    
def read_content():
    """Reading story or exiting """
    story = '''
        "A cellphone is found inside a sealed Egyptian tomb. What do you do?\na. Keep it\nb. Ignore It ",
        "A plane takes off with 81 passengers.It lands with 82. What do you do?\na. Question it\nb. Report to the airline",
        "As a joke, you use your cellphone to dial your own number.Someone pickup. How will you react\na. Scream\nb. Change your sim",
        "While on a leisurely stroll through the forest,you find strange footprints.Do you follow them?\na. I will follow them\nb. I will redirect from the path",
        "You briefly go out in the snow and come back inside.When you go out again,your footprint from earlier lead in a different direction. What do you do\na. Weary\nb. Scream"
    '''
    try:
        read_story = get_user_input("Enter Yes to proceed or No to quit: ", input_type=str)
        if read_story.isalpha() == 'Yes':
                  if read_story.isalpha() == 'No':
                        read_story = get_user_input("Enter the story name to proceed (e.g.,story.txt)", input_type=str)
                        with open('story.txt','a') as f:
                            f.write(story)
                        for file in ['story.txt']:
                            with open(file,'r') as f:
                                print(f)
    except ValueError:
            return read_content
                    
                                      
def thank_player():
    """The the playing for playing and encourage them"""
    display_message("\n Thank you for partaking. Please try a different choices in subsequent playthroughs.")
    
    
def main():
    """Main function to run the interactive story generator."""
    display_message("Welcome to the Interactive Story Generator!")
    player_name = get_user_input("Please enter your name: ")
    
    scene = setting_the_scene()
    role = character_creation()
    
    display_message(f"Welcome, {player_name}! Let's begin your adventure as the {role} in the {scene}.")
    
    display_message("\nPlot Development:")
    plot_development()
    
    display_message("\nOutcome:")
    possible_outcome()
    
    write_to_file()
    
    read_content()
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
    
        
        
    

    
        
            