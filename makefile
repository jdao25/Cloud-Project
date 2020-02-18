# Run the web server
runserver:
	@clear 
	@cd CloudProject && python3 manage.py runserver

# Opens the application in a web browser
# Note: Must run 'make runserver' before
open:
	@clear
	@# Line below can change depending on your preferred browser
	@firefox localhost:8000

# Open Project Folder in Atom 
# Can change depending on your preferred text editor
atom:
	@clear
	@cd .. && atom "Cloud-Project" && cd "Cloud-Project"
