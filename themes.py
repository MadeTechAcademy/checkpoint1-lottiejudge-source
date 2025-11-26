from duties import devops_apprenticeship_duty_list, BOOTCAMP, AUTOMATE
from jinja2 import Environment, FileSystemLoader

class Duties:
    def __init__(self, duties):
         self.duties = duties
   
    def template_creator(self, file_name, theme, title):
        env= Environment(loader = FileSystemLoader('templates'))
        template = env.get_template('template_duties.html')
        with open(file_name, 'w') as f:
            print(template.render(duties=theme, title=title), file = f)

    def bootcamp_duties(self):
        title = 'Bootcamp'
        theme = [self.duties[i] for i in BOOTCAMP]
        self.template_creator('bootcamp.html', theme, title)

    def automate_duties(self):
        title = 'Automate'
        theme = [self.duties[i] for i in AUTOMATE]
        self.template_creator('automate.html', theme, title)

    def create_duty_list(self):
        title = 'All Duties'
        theme = self.duties
        self.template_creator('all_duties.html', theme, title)
        for duty in self.duties:
           print("{0}\n".format(duty))


all_duties = Duties(devops_apprenticeship_duty_list)

if __name__=="__main__":
    user_duty_selection = input("""
    Welcome to apprentice themes!\n
    Press (1) to list all the duties\n
    Press (2) to list the duties from the Bootcamp\n
    Press (3) to list the duties from Automate\n                            
    Enter your choice:
    """)
    if user_duty_selection == '1':
        all_duties.create_duty_list()
    if user_duty_selection == '2':
        all_duties.bootcamp_duties()
    if user_duty_selection == '3':
        all_duties.automate_duties()


#  TODO: diff duties for diff times - testing
# TODO: flask front end innit - testing

# task three - dynamic theme name, dynamic naming of html file. 
# remove the input into it's own class? would that work? how many behaviours can you have in a singlwe class = could i have one for like all of them and then call it depening on which?
# remove any breaking of encapsulation and the hard coded stuff - hop;efully easier with dynamic namoing? 
# get CSS working
# hate the way the inputs done - look at that