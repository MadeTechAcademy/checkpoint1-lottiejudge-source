from jinja2 import Environment, FileSystemLoader

class Duties:
    def __init__(self, duties):
        self.duties = duties
        
    def template_creator(self, file_name, theme, title):
       
        env= Environment(loader = FileSystemLoader('templates'))
        template = env.get_template('template_duties.html')
        with open(f"renders/{file_name}.html", 'w') as f:
            print(template.render(duties=theme, title=title), file = f)
        print(f"{title}:\n")
        for duty in theme:
            print("{0}\n".format(duty))  