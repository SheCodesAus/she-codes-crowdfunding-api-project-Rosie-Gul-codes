Rosie's Crowdfunding project:
- Created an API to retrieve "Create" and "Update" about the crowdfunding project. This process applies to the entirety of the project.
- Implemented a "User Authentication" system 
- Implemented different authentication levels to allow access to the different parts of the API as follows: 
    a.	logged in
    b.	Logged out
    c.	Administrative status = Admin is the user.

API specification:
HTTP METHOD	URL	Purpose	Request Body	Successful Response Code	Authentication/Authorisation

PROJECTS					
GET	/projects/	Returns all projects	N/A	200	N/A
POST	/projects/	Create a new project	Project object	201	Must be logged in.
GET	/projects/1/	Returns the project with ID of “1”	N/A	200	N/A
PUT (edit/update)	/projects/1/	Updates the project with ID of “1”	Project object	201	Must be logged in.
Must be the project owner.
DELETE (by admin or owner only)	/projects/1	Deletes the project with ID of “1”	Project object OR N/A	200	Must be logged in.
Must be the project owner.

PLEDGES					
GET	/pledges/	Returns all pledges	N/A	200	N/A
POST 	/pledges/	Create a new pledge	Pledge object	201	Must be logged in.
Must not be the owner of the project.
GET	/pledges/1/	Get the pledge with ID of “1”	N/A	200	N/A
PUT	/pledges/1/	Updates the pledge with ID of “1”	Pledge object	201	Must be logged in.
Must be the pledge owner.
DELETE (by admin or owner only)	/pledges/1/	Deletes the pledge with ID of “1”	N/A	200	Must be logged in.
Must be the pledge owner.

USERS					
GET	/users/	Returns all users	N/A	200	
POST 	/users/	Creates a new user	User object	201	Must have unique username and a password to create an account
GET	/users/1/	Returns user profile with ID of “1”	N/A	200	N/A
DELETE (by admin(user) or owner only)	/pledges/1/	Deletes the user profile with ID of “1”	N/A	200	Must be logged in.
Must be the user.


GitHub Link:
https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-Rosie-Gul-codes

Heroku Link:
https://rosie-g-crowdfunding.herokuapp.com/projects/
https://rosie-g-crowdfunding.herokuapp.com/pledges/
https://rosie-g-crowdfunding.herokuapp.com/users/

NOTES:
1. projects/urls.py provides the pathways, 
urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view())
]
and the clues to identify what the next step is. Go to "projects/views.py" to view all relevant classes under the "projects" folder: 
views.ProjectList, views.ProjectDetail, views.PledgeList, views.PledgeDetail.
- View the code to define GET PUT POST DELETE
All projects = project list
Specific projects = project/id 
All pledges = pledge list
Specific pledges = pledge/id

2. Similarly, users/urls.py provides the pathways 
urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
]
and the clues to identify what the next step is.  Go to "users/views.py" to view all relevant classes under the "users" folder:  CustomUserList & CustomUserDetail.


3. serializers.py interprets a representation of the database and views.py send that readable representation to the browser.
- class ProjectSerializer(serializers.Serializer)
- class CustomUserDetailSerializer(CustomUserSerializer)
- class PledgeSerializer(serializers.Serializer)
- class PledgeDetailSerializer(PledgeSerializer)

4.	Migrations are a part of the process that allows Django to interpret the database correctly. The database is blank. We have created the “models.py” for Projects and Pledges.


Create users in Insomnia.
Run the server firstly.


