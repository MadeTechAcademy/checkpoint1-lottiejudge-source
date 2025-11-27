from duties import devops_apprenticeship_duty_list, BOOTCAMP, AUTOMATE, HOUSTON, GOING_DEEPER, ASSEMBLE, CALL_SECURITY
from jinja2 import Environment, FileSystemLoader

class Duties:
    def __init__(self, duties):
         self.duties = duties
   
    def template_creator(self, file_name, theme, title):
        env= Environment(loader = FileSystemLoader('templates'))
        template = env.get_template('template_duties.html')
        with open(f"renders/{file_name}", 'w') as f:
            print(template.render(duties=theme, title=title), file = f)
        for duty in theme:
            print("{0}\n".format(duty))

    def bootcamp_duties(self):
        title = 'Bootcamp'
        theme = [self.duties[i] for i in BOOTCAMP]
        self.template_creator('bootcamp.html', theme, title)

    def automate_duties(self):
        title = 'Automate'
        theme = [self.duties[i] for i in AUTOMATE]
        self.template_creator('automate.html', theme, title)
    
    def houston_duties(self):
        title = 'Houston, Prepare to Launch'
        theme = [self.duties[i] for i in HOUSTON]
        self.template_creator('houston.html', theme, title)
    
    def going_deeper_duties(self):
        title = 'Going Deeper'
        theme = [self.duties[i] for i in GOING_DEEPER]
        self.template_creator('going_deeper.html', theme, title)

    def assemble_duties(self):
        title = 'Assemble'
        theme = [self.duties[i] for i in ASSEMBLE]
        self.template_creator('assemble.html', theme, title)
    
    def call_security_duties(self):
        title = 'Call Security'
        theme = [self.duties[i] for i in ASSEMBLE]
        self.template_creator('call_security.html', theme, title)

    def create_duty_list(self):
        title = 'All Duties'
        theme = self.duties
        self.template_creator('all_duties.html', theme, title)



all_duties = Duties(devops_apprenticeship_duty_list)

if __name__=="__main__":
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

    


# TODO: move the print into a helper function/figure out how to print HTML to terminal? 
# TODO: add the created files to the git ignore - they don't need to be on github innit 
# TODO: look into encapsulation of it
# TODO: go over the read me and make sure it's done
# TODO: I feel like i could create a loop to populate and have one single function? or could I init it and then populate through that? but how would that word with user choice? it's pretty verbose
# I think if i make the duties into a class and store it there? 
# TODO: Look at the input and change that - start with tests. Move into it's own class I think? 

# task three - dynamic theme name, dynamic naming of html file. 
# remove the input into it's own class? would that work? how many behaviours can you have in a singlwe class = could i have one for like all of them and then call it depening on which?
# remove any breaking of encapsulation and the hard coded stuff - hop;efully easier with dynamic namoing? 
# get CSS working
# hate the way the inputs done - look at that