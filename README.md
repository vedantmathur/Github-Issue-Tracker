
# Simple Github Issue Browser

## The parameters and my assumptions
The task was to create a simple issue browser using the Github API pointed to an arbitrary repo. For this example I used Walmart's Thorax repository which has 30+ open issues. I hardcoded these parameters. 

When the app starts up, it displays a list of issues with some basic information, such as Title, Issue#, State, and Author. It displays it 10 at a time and uses spicing to paginate with previous and next buttons.

## The tools I used
I used Flask and Python for the backend computations and I used Jinja2 and HTML to make the frontend. All of this was developed in Pycharm on MacOS 10.15. There are other frameworks such as Django, however that might be excessive for a simple web app.

## Outstanding issues
- Currently, the application pulls the get request on every load of the start page, however that won't work if you have two instances of the application running- it could updated the data structure for all users, effectively disrupting their workflow.
- A large list of issues would overwhelm the server. We could go for a distributed backend or a larger server, or maybe pulling GET requests at intervals.
- It doesn't look too pretty.

## How this could be Improved
- Could switch to a more efficient method of getting the dictionaries from Json.
- Make it look prettier
- If this were to be far more powerful, we could have issue searching, kanban boards, etc.

## How to build it
To build and use this webapp, you will need 
- Python3.7
- requests (`pip install requests`)
- flask (`pip install flask`)
- json (`pip install json`)

use venv and run `python -m flask run`


### External Sources used:

Github's JSON structure for a sample repo
https://api.github.com/repos/walmartlabs/thorax/issues

What even is a GET Request
https://www.w3schools.com/tags/ref_httpmethods.asp

Quickstart to Flask (Python)
https://flask.palletsprojects.com/en/1.1.x/quickstart/

Quickstart to Jinja2 (the connection between HTML and Flask)
https://jinja.palletsprojects.com/en/2.11.x/

Rendering of variable
https://www.grantaguinaldo.com/rendering-variables-python-flask/

Redirecting to a URL
https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask

Recieving a param
https://stackoverflow.com/questions/9647586/getting-a-request-parameter-in-jinja2

