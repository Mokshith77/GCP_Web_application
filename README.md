# Web_app_Stockdatabase
            # ECS781P - CLOUD COMPUTING 2022
              #  Mini Project – Coursework
        INTRODUCTION
                The goal of the mini project is to apply and extend the techniques practiced during the labs, in order to build a prototype of a Cloud application.
                
                
The project has the form of an application, developed in Python and Flask.


The mini project works on the following aspects of Cloud applications:


REST-based service interface.


Interaction with external REST services.


Use of on an external Cloud database for persisting information.


Support for cloud scalability, deployment in a container environment.


Security Features.

#What is it? 


The application uses the yahoo finance API which gives the real time ticker data of stocks through the external API. The web application takes the input from the users and fetches the data and displays.


To demonstrate REST APIs CRUD operations, we are using MongoDB Atlas which is a cloud-based data base. 
To deploy our app on the GCP instance we used Kubernetes engine, and we created a cluster and connected with the GCP instance.
Prerequisites


In order to run the application, we need to have Python and Flask. We are also using Linux environment with the below commands.
First of all, we have to install Python:


sudo apt-get install python3-pip


Then, a virtual environment should be created:


python3 -m venv env


We will create docker image


sudo docker build -t karunkkrp/app:v2 .


We push the image to docker hub account


sudo docker push karunkkrp/app:v2


Create the cluster on the Kubernetes engine and configure with the GCP instance.


First intall kubctl in the cloud shell


Kubctl apply -f deploy.yaml



Kubctl apply -f service.yaml



Kubctl get svc 
