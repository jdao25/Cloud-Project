# Cloud-Project
This is a web application I created for my Big Data and Cloud Computing course. In doing this project, I will apply my knowledge on AWS S3 that I had learn from the course. The application was designed to allow the users to store their files within AWS S3 buckets. 


## Getting Started
For the best results, please use a Linux System. The project was created on a Linux environment and has not been fully run on other Operating Systems.
If you don't have Linux OS, I recommend you download VMware or VirtualBox and install a Linux distro for best results. 
We also recommend you open the application using Firefox as your browser. 


### Prerequisites
- Python 3.7.5
- OpenCV 4.1.2
- Django 3.0 
- Pillow 
- Django storages 
- Django crispy Forms <br /><br />
"Required packages will be install when run 'pip install -r requirements.txt'"


### Installing
1) (Optional but recommended) Use Linux OS
2) Install a virtual environment
3) Download the project source code to your virtual environment. 
4) Run "pip install -r requirements.txt" to install necessary project packages. 
5) cd to "Cloud-Project" (same directory as makefile)
6) Run "make" to run the server
7) Type localhost:8000 in firefox 


## Deployment

1) Create Heroku Account
2) Run "heroku create application-name"
3) Create Procfile
4) Change "STATIC_ROOT" to "staticfiles"
5) Run "git push heroku master"


## Built With
* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework used


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
