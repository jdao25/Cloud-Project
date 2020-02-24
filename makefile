# Run the web server
runserver:
	@clear 
	@cd CloudApp && python3 manage.py runserver

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

# ----- DELETE ON PUBLISH ----- #
# This opens up github on google chrome
github:
	@clear
	@google-chrome https://github.com/jdao25/Cloud-Project

# This will open up Corey Schafer's Django tutorial
video:
	@google-chrome https://www.youtube.com/watch?v=a48xeeo5Vnk
