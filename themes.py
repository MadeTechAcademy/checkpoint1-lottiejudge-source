from duties import devops_apprenticeship_duty_list
from jinja2 import Environment, FileSystemLoader

class Duties:
    def __init__(self, duties):
         self.duties = duties
         
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
    Enter your choice:
    """)
    if user_duty_selection == '1':
        all_duties.create_duty_list()

#  TODO: Can i sepearte out the input from the class? is that necessary 
# TODO:L https://www.geeksforgeeks.org/python/getting-started-with-jinja-template/ - this should hopefully make the ninja syntax shorter?
#  TODO: Make HTML better using CSS file. Test this? Should i like test it;s in futura etc?
#  TODO: diff duties for diff times - testing
# TODO: flask front end innit - testing

# task three - dynamic theme name, dynamic naming of html file. 
# remove the input into it's own class? would that work? how many behaviours can you have in a singlwe class = could i have one for like all of them and then call it depening on which?
# remove any breaking of encapsulation and the hard coded stuff - hop;efully easier with dynamic namoing? 
# get CSS working
# hate the way the inputs done - look at that