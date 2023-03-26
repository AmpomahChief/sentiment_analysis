# Project : Natural Language Processing (NLP)

## Description

This repository contains a project on NLP. The objective is to build a sentiment analysis model for COVID 19 tweets to determine whether the tweets are Positive, Negative or Nutral. 

This project also contains a Gradio app to deploy the trained model.

## Setup
Install the required packages to be able to run the evaluation locally.

You need to have [`Python3`](https://www.python.org/) on your system. Then you can clone this repo and being at the repo's root (`root :: repo_name> ...`)  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

The both long command-lines have a same structure, they pipe multiple commands using the symbol **;** but you may manually execute them one after another.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;

2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;

3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;

4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.

**NB:** For MacOs users, please install `Xcode` if you have an issue.


## EXCUTION
Excute the command below to run the app. 

        gradio gradioapp/py


## SCREENSHOOTS

![](/screenshoots/GradioSent1.png)

![](/screenshoots/GradioSent2.png)

![](/screenshoots/GradioSent3.png)




