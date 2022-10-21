How to use the script ELI5:

- donwload python at https://www.python.org/downloads/
- open your terminal at a place you want to dowload the script (eg an empty folder on Desktop)

=> in terminal type the following commands:

git clone https://github.com/burnfiat4jpegs/free.git
cd free
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt

=> we've just created a virtual environment for python and downloaded the dependancies
=> now we need to configure free.py to use your own twitter account. 

=> go to https://developer.twitter.com/en/portal/petition/essential/basic-info and follow the steps to create your twitter developper account. Enter "making a bot" as the usecase. 
=> you arrive at the dev portal. Enter an app name (random or whatever you want). After that, you should have access to api key, api secret and bearer token. Save them
=> you arrive at your personal dashboard. click on the left pane "Projects & Apps" => your app name
=> At the "User authentication settings" level, click on "Set up". Then for the required fields:
    - "Read and Write"
    - "Native App"
    - "https://localhost"
    - "https://nowebsite.com" then save (the other fields can remain empty)

=> you can save the "Client ID" and "Client Secret" infos just in case but we won't need it
=> Next, click on the middle top of the screen "Keys and tokens"
=> At the "Access token and Secret", click "generate"
=> Save the "Access token" and "Access token Secret" infos. After than, you should have "Created with Read and Write permissions" written on the "Access Token and Secre" case

Now you have all the infos needed:
    - api key
    - api secret 
    - bearer token 
    - access token  
    - access token secret 

=> open free.py with a text editor
=> In the CONFIGURATION block, replace the fields with all the twitter infos you just gathered

And voila

To run the script run in terminal :

python3 free.py 

Enjoy



