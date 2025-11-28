from themes import Duties
from duties import devops_apprenticeship_duty_list

all_duties = Duties(devops_apprenticeship_duty_list)

class User_option:    
    def print_options(self):
         user_duty_selection = input("""
            Welcome to apprentice themes!\n
            Press (1) to list all the duties\n
            Press (2) to list the duties from the Bootcamp\n
            Press (3) to list the duties from Automate\n  
            Press (4) to list the duties from Houston, Prepare to Launch\n   
            press (5) to list the duties from Going Deeper\n
            press (6) to list the duties from Assemble\n
            press (7) to list the duties from Call Security\n                                                
            Enter your choice:
            """)
         if user_duty_selection == '1':
                    all_duties.create_duty_list()
         if user_duty_selection == '2':
                    all_duties.bootcamp_duties()
         if user_duty_selection == '3':
                    all_duties.automate_duties()
         if user_duty_selection == '4':
                    all_duties.houston_duties()
         if user_duty_selection == '5':
                    all_duties.going_deeper_duties()
         if user_duty_selection == '6':
                    all_duties.assemble_duties()
         if user_duty_selection == '7':
                    all_duties.call_security_duties()


if __name__=="__main__":
    duties_menu = User_option()
    duties_menu.print_options()



# TODO: I feel like i could create a loop to populate and have one single function? or could I init it and then populate through that? but how would that word with user choice? it's pretty verbose
# I think if i make the duties into a class and store it there- maybe a dictionary? dictionaries seemed to be considered bad on clean code? 
#  

