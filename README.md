# T5_Translation_Cloud_Deployment_with_Azure_and_Docker
End-to-End Deep Learning project making use of the "T5-small" transformers model and pushing the FastAPI and Docker created webserver to the cloud.

# Project Description: Deep Learning Translation API with FastAPI and Docker

**Important Note** 
For now I have made this project description with ChatGPT, ofcourse I gave it the main components and a baseline and after letting gpt describe the project I made, it is actually not a bad description to start, I will change this later. This was also possible because I have made sure to descripe all of the processes in the files themselves seperately. Whenever there are any questions, feel free to send me a message! 

This project aims to develop an end-to-end deep learning translation system using the T5 transformers model. The system will be deployed as a web server using FastAPI and Docker. Users will be able to send translation requests through the API and receive the translated text as a response.

The project involves the following components:

**Main Functionality:** The core functionality of the system is to provide translations from one language to another. Users will send translation requests containing the text to be translated, the base language, and the target language. The system will store the translation request in a database and run the T5 model to generate the translated text.

**FastAPI Web Server:** The translation system will be exposed as a web server using FastAPI, a high-performance web framework. The server will define several routes to handle different actions, such as submitting translation requests and retrieving translation results. The routes will be implemented in the main.py file.

**Database Integration:** To store translation requests and their corresponding translations, the project will utilize a database. The Peewee ORM will be used to define a TranslationModel class representing the database table. Each translation request will have attributes such as the text to be translated, the base language, the target language, and the generated translation.

**T5 Transformers Model:** The T5 transformers model, a state-of-the-art deep learning model for text generation, will be used for the translation task. The model will be loaded using the Hugging Face library, and its pre-trained weights will be used for translation. The T5 tokenizer will also be used to preprocess the text before feeding it to the model.

**Background Tasks:** To handle the translation process asynchronously, background tasks will be employed. When a translation request is received, a background task will be added to the queue, which will run the translation process in the background. This allows the server to handle multiple translation requests simultaneously without blocking the main execution.

**Docker Containerization:** The entire translation system, including the web server, database, and model dependencies, will be packaged into a Docker container. The Dockerfile provided in the project will define the necessary steps to build the container, including installing dependencies and configuring the environment. This ensures that the project can be easily deployed on any machine with Docker support.

**Deployment to Azure (Optional):** In addition to local deployment with Docker, the project can be deployed to the Azure cloud platform. Azure Container Registry and Azure Web App for Containers can be utilized to containerize and host the application. This allows for scalable and accessible deployment on the cloud.
