
ALL_DUTIES = [
    "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.",
    "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members.",
    "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review.",
    "Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture.",
    "Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts.",
    "Duty 6 Implement and improve release automation & orchestration, often using Application Programming Interfaces (API), as part of a continuous delivery and continuous deployment pipeline, ensuring that team(s) are able to deploy new code rapidly and safely.",
    "Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers).", "Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance.",
    "Duty 9 Apply leading security practices throughout the Software Development Lifecycle (SDLC).",
    "Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable.",
    "Duty 11 Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications.",
    "Duty 12 Look to automate any manual tasks that are repeated, often using APIs.",
    "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience.",
]
BOOTCAMP = [0, 1, 2, 3, 12]
AUTOMATE = [4, 6, 9]
HOUSTON = [5, 6, 9, 11]
GOING_DEEPER = [10]
ASSEMBLE = [7]
CALL_SECURITY = [8]

BOOTCAMP_THEME = {
    'self' :'Bootcamp',
    'file_name' : 'bootcamp',
    'theme' :  [ALL_DUTIES[i] for i in BOOTCAMP],
    'title' : 'Bootcamp'
}

AUTOMATE_THEME = {
    'self' :'Automate',
    'file_name' : 'automate',
    'theme' :  [ALL_DUTIES[i] for i in AUTOMATE],
    'title' : 'Automate'
}

HOUSTON_THEME = {
    'self' :'Houston',
    'file_name' : 'houston',
    'theme' :  [ALL_DUTIES[i] for i in HOUSTON],
    'title' : 'Houston, Prepare to Launch'
}

GOING_DEEPER_THEME = {
    'self' :'Going Deeper',
    'file_name' : 'going_deeper',
    'theme' :  [ALL_DUTIES[i] for i in GOING_DEEPER],
    'title' : 'Going Deeper'
}

ASSEMBLE_THEME = {
    'self' :'Assemble',
    'file_name' : 'assemble',
    'theme' :  [ALL_DUTIES[i] for i in ASSEMBLE],
    'title' : 'Assemble'
}

CALL_SECURITY_THEME = {
    'self' :'Call Security',
    'file_name' : 'call_security',
    'theme' :  [ALL_DUTIES[i] for i in CALL_SECURITY],
    'title' : 'Call Security'
}

ALL_DUTIES_THEME = {
    'self' :'All Duties',
    'file_name' : 'all_duties',
    'theme' :  ALL_DUTIES,
    'title' : 'All Duties'
}







