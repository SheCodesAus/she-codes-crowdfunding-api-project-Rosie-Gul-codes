
Projects / urls
Users/urls
come back to projects to look at paths and explore all options exist in the paths e.g project/id
(project details)
this provides clues to what the next step is e.g find the following class: views.ProjectDetail
go to views to locate selected project detail
Identify what code is used to define GET PUT POST DELETE
PROJECTS OR PROJECTS/ID THEN VIEWS

Cretaingg users in insomnia
dint forget to run the server

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view()),


Go to urls to see pathways into the website.
#urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('cprojes/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view()),