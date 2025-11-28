from themes import ALL_DUTIES, BOOTCAMP, AUTOMATE, HOUSTON, GOING_DEEPER, ASSEMBLE, CALL_SECURITY
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
        theme = [self.duties[i] for i in CALL_SECURITY]
        self.template_creator('call_security.html', theme, title)

    def create_duty_list(self):
        title = 'All Duties'
        theme = self.duties
        self.template_creator('all_duties.html', theme, title)



