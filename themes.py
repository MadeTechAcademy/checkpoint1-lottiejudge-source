from duties import devops_apprenticeship_duty_list

class Duties:
    def __init__(self, duties):
         self.duties = duties
         
    def create_duty_list(self):
        for duty in self.duties:
            filename = "all_duties.html"
            content = template.render(
                duty=duty
            )
            with open(filename, mode="w", encoding="utf-8") as message:
                message.write(content)
            print("{0}\n".format(duty))
        duty_list +='</ul>'
        create_doc.write(f"<html>\n<head>\n<title> \n Duty Selection \n</title>\n</head>\n <body>\n{duty_list}\n</body>\n</html>")

all_duties = Duties(devops_apprenticeship_duty_list)

if __name__=="__main__":
    user_duty_selection = input("""
    Welcome to apprentice themes!\n
    Press (1) to list all the duties\n
    Enter your choice:
    """)
    if user_duty_selection == '1':
        all_duties.create_duty_list()

#  TODO: HTML file and testing - do this first? See if pattern emerges? 
#  TODO: diff duties for diff times - testing
# TODO: flask front end innit - testin