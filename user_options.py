from duties import Duties
from themes import BOOTCAMP_THEME, ALL_DUTIES_THEME, AUTOMATE_THEME, HOUSTON_THEME, GOING_DEEPER_THEME, ASSEMBLE_THEME, CALL_SECURITY_THEME

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
         theme_selection = {
                 '1': ALL_DUTIES_THEME,
                 '2': BOOTCAMP_THEME,
                 '3': AUTOMATE_THEME,
                 '4': HOUSTON_THEME,
                 '5': GOING_DEEPER_THEME,
                 '6': ASSEMBLE_THEME,
                 '7': CALL_SECURITY_THEME
         }
         if user_duty_selection in theme_selection:
                return Duties.template_creator(**theme_selection.get(user_duty_selection))
         else: print('incorrect selection')
                  
if __name__=="__main__":
    duties_menu = User_option()
    duties_menu.print_options()
