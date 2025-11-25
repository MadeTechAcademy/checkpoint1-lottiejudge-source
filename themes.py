from duties import devops_apprenticeship_duty_list
from jinja2 import Template

class Duties:
    def __init__(self, duties):
         self.duties = duties
         
    def create_duty_list(self):
        File = open('templates/template_duties.html', 'r')
        content = File.read()
        File.close()
        duty_list = '<ul>\n'
        for duty in self.duties:
            duty_list += '<li>{}</li>\n'.format(duty)
            print("{0}\n".format(duty))
        duty_list +='</ul>'
        template = Template(content)
        rendered_form = template.render(duty_list=duty_list)
        output = open('all_duties.html', 'w')
        output.write(rendered_form)
        output.close()

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