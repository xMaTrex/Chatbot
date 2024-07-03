Entwickler:
Max Tremmel
811970

- Prüfungsleistung Master Wirtschaftsinformatik Sommersemester 2024 -

Dieser Chatbot wurde im Modul: Knowledge Representation & Natural Language Processing entwickelt.

---------------------------------------------

Der Chatbot basiert auf dem Open-Source Framework RASA.
Umsetzung mittels 'Python Version: 3.8'

Projektstruktur / Ordnerstruktur:

    /actions:   	    custom actions for the chatbot
    /data:      	    training data for the chatbot
      nlu.yml:      	intents with examples, extract relevant information
      rules.yml:    	ruled based actions
      stories.yml:  	possible story paths
    /models:    	    trained chatbot models
    /templates:		    html page for browser
    /tests:     	    testing the chatbot
    app.py:		        Flask Framework + webhook
    config.yml:     	configuration settings
    credentials.yml:	credentials the chatbot is using
    domain.yml:     	intents, responses, session_config
    endpoints.yml:  	servers, url, ...

---------------------------------------------

rasa documentation: https://rasa.com/docs/rasa/

How to run it:

1. download files
2. unzip them
3. start virtual environment (terminal: ".\.venv\Scripts\activate")
4. (train RASA chatbot (terminal: "rasa train")
5. start action server (terminal: "rasa run actions")
6. start rasa server (terminal: "rasa run") (in a new terminal)
7. run app.py
8. open in browser: probably "http://127.0.0.1:5000/" but check console after app.py is running
9. close, shut down everything
10. deactivate venv (terminal: "deactivate")

---------------------------------------------
