from duties import Duties
from themes import ALL_DUTIES, BOOTCAMP_THEME, ALL_DUTIES_THEME, AUTOMATE_THEME, HOUSTON_THEME, GOING_DEEPER_THEME, ASSEMBLE_THEME, CALL_SECURITY_THEME

# all_duties = Duties(ALL_DUTIES)

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
                    Duties.template_creator(**ALL_DUTIES_THEME)
         if user_duty_selection == '2':
                    Duties.template_creator(**BOOTCAMP_THEME)
         if user_duty_selection == '3':
                   Duties.template_creator(**AUTOMATE_THEME)
         if user_duty_selection == '4':
                    Duties.template_creator(**HOUSTON_THEME)
         if user_duty_selection == '5':
                    Duties.template_creator(**GOING_DEEPER_THEME)
         if user_duty_selection == '6':
                    Duties.template_creator(**ASSEMBLE_THEME)
         if user_duty_selection == '7':
                    Duties.template_creator(**CALL_SECURITY_THEME)
                    


if __name__=="__main__":
    duties_menu = User_option()
    duties_menu.print_options()



# TODO: I feel like i could create a loop to populate and have one single function? or could I init it and then populate through that? but how would that word with user choice? it's pretty verbose
# I think if i make the duties into a class and store it there- maybe a dictionary? dictionaries seemed to be considered bad on clean code? 
#  

