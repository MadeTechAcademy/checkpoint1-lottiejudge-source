from themes import Duties
from user_options import User_option
from duties import devops_apprenticeship_duty_list

correct_list_of_duties = ["Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.",
    "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members.", 
    "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review.", "Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture.", 
    "Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts.", "Duty 6 Implement and improve release automation & orchestration, often using Application Programming Interfaces (API), as part of a continuous delivery and continuous deployment pipeline, ensuring that team(s) are able to deploy new code rapidly and safely.",
    "Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers).", 
    "Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance.",
    "Duty 9 Apply leading security practices throughout the Software Development Lifecycle (SDLC).",
    "Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable.",
    "Duty 11 Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications.",
    "Duty 12 Look to automate any manual tasks that are repeated, often using APIs.", "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience."
    ]
devops_duty_one_string =  "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage."

def test_duty_list():
    assert len(devops_apprenticeship_duty_list) == 13
    assert devops_apprenticeship_duty_list == correct_list_of_duties

def test_all_duty_list_terminal_output(capsys):
    duty_test_instance = Duties(correct_list_of_duties)
    duty_test_instance.create_duty_list()
    captured = capsys.readouterr()
    assert correct_list_of_duties[0] in captured.out

def test_duties_to_HTML_output():
    file = open("renders/all_duties.html", 'r')
    assert devops_duty_one_string in file.read()

def test_bootcamp_to_HTML():
    duty_test_instance = Duties(correct_list_of_duties)
    duty_test_instance.bootcamp_duties()
    file = open("renders/bootcamp.html", 'r')
    assert correct_list_of_duties[0] in file.read()

def test_automate_to_HTML():
    duty_test_instance = Duties(correct_list_of_duties)
    duty_test_instance.automate_duties()
    file = open("renders/automate.html", 'r')
    assert correct_list_of_duties[0] not in file.read()

def test_houston_to_HTML():
    theme_title = 'Houston, Prepare to Launch'
    duty_test_instance = Duties(correct_list_of_duties)
    duty_test_instance.houston_duties()
    file = open("renders/houston.html", 'r')
    assert theme_title in file.read()

def test_going_deeper_to_HTML():
    theme_title = 'Going Deeper'
    duty_test_instance = Duties(correct_list_of_duties)
    duty_test_instance.going_deeper_duties()
    file = open("renders/going_deeper.html", 'r')
    assert theme_title in file.read()

def test_assemble_to_HTML():
    theme_title = 'Assemble'
    duty_test_instance = Duties(correct_list_of_duties)
    duty_test_instance.assemble_duties()
    file = open("renders/assemble.html", 'r')
    assert theme_title in file.read()

def test_call_security_to_HTML():
    theme_title = 'Call Security'
    duty_test_instance = Duties(correct_list_of_duties)
    duty_test_instance.call_security_duties()
    file = open("renders/call_security.html", 'r')
    assert correct_list_of_duties[8] in file.read()

# write a test for the input being in a seperate file and then being called using the method. Import etc? 
def test_user_input_prints(capsys, monkeypatch):
    monkeypatch.setattr('print_options.input')
    test_instance = User_option()
    test_instance.print_options()
    captured = capsys.readouterr()
    assert 'Welcome to apprentice themes!\n' in captured

