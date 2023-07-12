# T5_Translation_Cloud_Deployment_with_Azure_and_Docker
End-to-End Deep Learning project making use of the "T5-small" transformers model and pushing the FastAPI and Docker created webserver to the cloud with Azure.

# Project Description: Deep Learning Translation API with FastAPI and Docker

This project aims to develop an end-to-end deep learning translation system using the T5 transformers model. The system will be deployed as a web server using FastAPI and Docker. Users will be able to send translation requests through the API and receive the translated text as a response.

The project involves the following components:

**Main Functionality:** The core functionality of the system is to provide translations from one language to another. Users will send translation requests containing the text to be translated, the base language, and the target language. The system will store the translation request in a database and run the T5 model to generate the translated text.

**FastAPI Web Server:** The translation system will be exposed as a web server using FastAPI, a high-performance web framework. The server will define several routes to handle different actions, such as submitting translation requests and retrieving translation results. The routes will be implemented in the main.py file.

**Database Integration:** To store translation requests and their corresponding translations, the project will utilize a database. The Peewee ORM will be used to define a TranslationModel class representing the database table. Each translation request will have attributes such as the text to be translated, the base language, the target language, and the generated translation.

**T5 Transformers Model:** The T5 transformers model, a state-of-the-art deep learning model for text generation, will be used for the translation task. The model will be loaded using the Hugging Face library, and its pre-trained weights will be used for translation. The T5 tokenizer will also be used to preprocess the text before feeding it to the model.

**Background Tasks:** To handle the translation process asynchronously, background tasks will be employed. When a translation request is received, a background task will be added to the queue, which will run the translation process in the background. This allows the server to handle multiple translation requests simultaneously without blocking the main execution.

**Docker Containerization:** The entire translation system, including the web server, database, and model dependencies, will be packaged into a Docker container. The Dockerfile provided in the project will define the necessary steps to build the container, including installing dependencies and configuring the environment. This ensures that the project can be easily deployed on any machine with Docker support.

**Deployment to Azure (Optional):** In addition to local deployment with Docker, the project can be deployed to the Azure cloud platform. Azure Container Registry and Azure Web App for Containers can be utilized to containerize and host the application. This allows for scalable and accessible deployment on the cloud.


**I have made sure to describe all of the processes I went trough in the files themselves seperately!** 

# Files and their Usecases 

main.py: This file contains the routes for the web server implemented using FastAPI. It defines three routes: "/" for testing the server, "/translate" for submitting translation requests, and "/results" for retrieving the translated text.

tasks.py: This file contains the logic for saving and executing translations. It utilizes the T5 Transformers model to perform the text translation. The translations are stored in a SQLite database using the Peewee ORM framework.

model.py: This file defines the database model for storing translations. It utilizes the Peewee library to manage the interaction with the SQLite database.

Dockerfile: This file contains the instructions for building a Docker container for the project. It starts by basing the container on the Python 3.10 image, copies the project files into the working directory, installs the required libraries, and sets the command to run the FastAPI server.

# Steps to run the project:

Install Docker on your system if you haven't done so already.

Create a new project directory on your local machine and place the files main.py, tasks.py, model.py, requirements.txt, and Dockerfile in this directory.

Open a terminal window and navigate to the project directory.

Build the Docker container using the following command:

shell
Copy code
docker build -t deep_learning_with_fastapi .
Wait for the build process to complete. This may take some time depending on your system and internet connection.

Run the Docker container using the following command:
shell
Copy code
docker run -d --name deep_learning_with_fastapi -p 80:80 deep_learning_with_fastapi
Check if the container is successfully running using the following command:
shell
Copy code
docker ps
You should see the started container deep_learning_with_fastapi in the list of active containers.

Open a web browser and go to http://localhost. You should see the FastAPI web server and have access to the available endpoints.
With these steps, you can run the Deep Learning Translation project locally using Docker.

# To deploy the project on Azure, you need to follow these steps:

Create an Azure account if you don't have one already.

Create a new Azure Container Registry (ACR) resource in the Azure Portal. This will register your Docker container for deployment on Azure.

Rebuild your Docker container with a tag referencing your Azure Container Registry. For example:

bash
Copy code
docker build -t <acrName>.azurecr.io/deep_learning_with_fastapi .
Push the Docker container to your Azure Container Registry using the following command:
bash
Copy code
docker push <acrName>.azurecr.io/deep_learning_with_fastapi
Create a new Azure Web App for Containers resource in the Azure Portal. Configure it to use the Docker container from your Azure Container Registry.

Deploy your Azure Web App for Containers and wait for the deployment to complete.

After deployment, you can access the FastAPI web server through the URL of your Azure Web App.

These are the basic steps to deploy the project on Azure using Azure Container Registry and Azure Web App for Containers. Note that you may need to perform additional configurations and customizations depending on your specific requirements and the Azure services you intend to use.

Make sure to set up the necessary security and access controls for your Azure resources to ensure the security of your application.

# How to view your databse, the made translations and their index 

To view the contents of the database file "translations.db" and examine all the translated texts along with their indexes, follow the steps below:

Open a terminal window.
Navigate to the project directory where the "translations.db" file is located.
Run the following command to start the SQLite command-line shell and connect to the database:
shell
Copy code
sqlite3 translations.db
Once connected, you can execute SQL queries to retrieve and view the data. For example, you can use the following command to display all the records in the TranslationModel table:
shell
Copy code
SELECT * FROM TranslationModel;
This will show you the text, base language, wanted language, and translation fields for each translation entry.

You can use various SQL commands and queries to manipulate and analyze the data in the database. Refer to the SQLite documentation (https://sqlite.org/docs.html) for more information on working with SQLite databases.


