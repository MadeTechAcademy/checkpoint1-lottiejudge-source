from duties import devops_apprenticeship_duty_list, BOOTCAMP, AUTOMATE
from jinja2 import Environment, FileSystemLoader

class Duties:
    def __init__(self, duties):
         self.duties = duties

    
    def bootcamp_duties(self):
        theme = [self.duties[i] for i in BOOTCAMP]
        env= Environment(loader = FileSystemLoader('templates'))
        template = env.get_template('template_duties.html')
        with open('bootcamp.html', 'w') as f:
            print(template.render(duties=theme), file = f)

    def automate_duties(self):
        theme = [self.duties[i] for i in AUTOMATE]
        env= Environment(loader = FileSystemLoader('templates'))
        template = env.get_template('template_duties.html')
        with open('automate.html', 'w') as f:
            print(template.render(duties=theme), file = f)



    def create_duty_list(self):
        env= Environment(loader = FileSystemLoader('templates'))
        template = env.get_template('template_duties.html')
        with open('all_duties.html', 'w') as f:
            print(template.render(duties=self.duties), file = f)
            
        for duty in self.duties:
            print("{0}\n".format(duty))


all_duties = Duties(devops_apprenticeship_duty_list)

if __name__=="__main__":
    user_duty_selection = input("""
    Welcome to apprentice themes!\n
    Press (1) to list all the duties\n
    Press (2) to list the duties from the Bootcamp\n
    Press (3) to list the dutie from Automate\n                            
    Enter your choice:
    """)
    if user_duty_selection == '1':
        all_duties.create_duty_list()
    if user_duty_selection == '2':
        all_duties.bootcamp_duties()
    if user_duty_selection == '3':
        all_duties.automate_duties()

#  TODO: Make HTML better using CSS file. Test this? Should i like test it;s in futura etc?
#  TODO: diff duties for diff times - testing
# TODO: flask front end innit - testing

# task three - dynamic theme name, dynamic naming of html file. 
# remove the input into it's own class? would that work? how many behaviours can you have in a singlwe class = could i have one for like all of them and then call it depening on which?
# remove any breaking of encapsulation and the hard coded stuff - hop;efully easier with dynamic namoing? 
# get CSS working
# hate the way the inputs done - look at that