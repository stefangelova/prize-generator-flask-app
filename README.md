# QA Project 2

## Introduction 
 
 For this project I have created a web application using Python and Flask, with four distinct services, one generating random numbers
 and another random letters. Those two services get requested into the backend service and generate a prize from a set prize list.
 That output gets requested and displayed by the frontend and saved into the database. In addition there are two more services a mysql
 database where the generated values get saved and nginx which acts as a load balancer.

## Risk Assesment 

![Risk Assessment](https://github.com/stefangelova/project2/blob/master/documentation/Capture.PNG)

## CI Pipeline 

![CI Pipeline](https://github.com/stefangelova/project2/blob/master/documentation/Untitled%20Diagram%20(2).jpg)

## Technologies used:

 + Python
 + FLask
 + MySQL
 + GitHub
 + [Trello](https://trello.com/b/IhLz0K3P/qa2)
 + Docker (Compose and Swarm)
 + Jenkins
 + Ansible
 + NGINX
 + Azure
 + Pytest
 
## Service Structure

![ServStruct](https://github.com/stefangelova/project2/blob/master/documentation/Untitled%20Diagram%20(3).jpg)


## Encountered Issues 

Due to unforseen technical circumstances, the progress of the project was hindered, in addition to my lack of familiarity with the technologies I was working with.
 
## Sprints

I planned to conduct 3 sprints which I planned through [Trello](https://trello.com/b/IhLz0K3P/qa2). 
 + In the first sprint I created the random generator services and the backend service as well as deployed them with docker compose in order to test them.
 + In the second sprint I finished creating all services and worked on deploying them with docker compose and docker swarm.
 + In the third sprint, there was much less development as my work on Jenkins, Ansibe and the testing was largely unsuccessful.
 
 
## Future Improvements 

I would like to complete the tasks from the backlog which I could not as well as improve the UI. In addition I would like to improve my skills in Ansible and Jenkins.


 
 -----------------------------------------------------------------------------
The application can be accessed by clicking [here](http://51.104.16.150)


