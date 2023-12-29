# Chatbot_GPt4_Streamlit

OpenAI and Streamlit Chatbot

This repository contains the code for a chatbot powered by OpenAI's GPT model, interfaced through Streamlit. The chatbot is designed to provide users with an interactive and engaging experience, leveraging the advanced natural language understanding capabilities of OpenAI's models. Users can ask questions, get assistance, or even have a casual conversation with the bot. This project aims to explore the realms of AI-driven chat interfaces and demonstrates the integration of OpenAI with Streamlit for an efficient and user-friendly application.

*** Please remember to add a folder names .streamlit in the project directory and include your OpenAI API code in it, Save the file in the .streamlit folder as secrets.toml***
<--------------------------------------------------------------------------------------------------------------->

## Set up your Environment


### **`macOS`** type the following commands : 

- For installing the virtual environment you can either use the [Makefile](Makefile) and run `make setup` or install it manually with the following commands:

     ```BASH
    make setup
    ```
    After that active your environment by following commands:
    ```BASH
    source .venv/bin/activate
    ```
Or ....
- Install the virtual environment and the required packages by following commands:

    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
    
### **`WindowsOS`** type the following commands :

- Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-bash` CLI :
    ```
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    **`Note:`**
    If you encounter an error when trying to run `pip install --upgrade pip`, try using the following command:
    ```Bash
    python.exe -m pip install --upgrade pip
    ```

    ### **`Linux Users`**  : You know what to do :sunglasses:
