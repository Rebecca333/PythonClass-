# Challenge Level: Advanced

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You took a survey of all of the employees at your organization to see what their twitter and github names were. You got a few responses.
#   You have two spreadsheets in CSV (comma separated value) format:
#       all_employees.csv: See section_07_(files).  Contains all of the employees in your organization and their contact info.
#           Columns: name, email, phone, department, position
#       survey.csv: See section_07_(files).  Contains info for employees who have completed a survey.  Not all employees have completed the survey.
#           Columns: email, twitter, github

# Challenge 1: Open all_employees.csv and survey.csv and compare the two.  When an employee from survey.csv appears in all_employees.csv, print out the rest of their information from all_employees.csv.

# Sample output:
#       Shannon Turner took the survey! Here is her contact information: Twitter: @svt827 Github: @shannonturner Phone: 202-555-1234

# Challenge 2: Add the extra information from survey.csv into all_employees.csv as extra columns.  
# IMPORTANT: It would probably be a good idea to save it as an extra file instead of accidentally overwriting your original!
# By the end, your all_employees.csv should contain the following columns: name, email, phone, department, position, twitter, github

with open("all_employees.csv", "r") as employees:
	employees_list = employees.read().split("\n")
with open ("surveys.csv", "r") as surveys:
	survey_list = surveys.read().split("\n")
for employees_index, employee in enumerate(employees_list):
	employees_list [employees_index]=employee.split(", ")
for survey_index, survey in enumerate(survey_list):
	survey_list [survey_index]=survey.split(",")
employees_headers = employees_list.pop(0)
survey_headers = survey_list.pop(0)

employees_dictionary = {}
surveys_dictionary = {}
print employees_headers
print survey_headers

for index, emp in enumerate(employees_list):
	name = emp[employees_headers.index("name")]
	employees_dictionary[name] = {}
	email = emp[employees_headers.index("email")]
	employees_dictionary[name]["email"] = email
	phone = emp[employees_headers.index("phone")]
	employees_dictionary[name]["phone"] = phone
	department = emp[employees_headers.index("department")]
	employees_dictionary[name]["department"] = department
	position = emp[employees_headers.index("position")]
 	employees_dictionary[name]["position"] = position
for index, surv in enumerate(survey_list):
	survey_key = "survey {0}".format(index + 1)
	surveys_dictionary[survey_key] = {}
	email = surv[survey_headers.index("email")]
	surveys_dictionary[survey_key]["email"] = email
	twitter = surv[survey_headers.index("twitter")]
	surveys_dictionary[survey_key]["twitter"] = twitter
	github = surv[survey_headers.index("github")]
	surveys_dictionary[survey_key]["github"] = github

full_employees_dictionary = employees_dictionary

for name, info in employees_dictionary.items():
	email_address = info.get("email")
	for survey_num, survemail in surveys_dictionary.items():
		if survemail.get("email") == email_address:
			print """{0} took the survey! Here is her contact information: Twitter: {1}, Github: {2}, Email: {3}""".format(name,survemail.get("twitter"),survemail.get("github"),email_address)

for name, info in employees_dictionary.items():
	email_address = info.get("email")
	for survey_num, survemail in surveys_dictionary.items():
		if survemail.get("email") == email_address:
			full_employees_dictionary[name]["twitter"] = survemail.get("twitter")
			full_employees_dictionary[name]["github"] = survemail.get("github")

output = "Name, Email, Phone, Department, Position,Twitter, Github"

for name, info in full_employees_dictionary.items():
	email = info.get("email", "")
	phone = info.get("phone","")
	department = info.get("department","")
	position = info.get("position","")
	twitter = info.get("twitter","")
	github = info.get("github","")
	output += "\n{0}, {1}, {2}, {3}, {4}, {5}, {6}".format(name,email,phone,department,position,twitter,github)

print output

with open("alll_the_employees.csv", "w") as new_file:
	new_file.write(output)
