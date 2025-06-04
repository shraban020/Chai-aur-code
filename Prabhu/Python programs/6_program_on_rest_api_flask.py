"""
Documentation:
    -    https://pypi.org/project/Flask/
    -   https://pypi.org/project/fastapi/
    -   https://pypi.org/project/Django/

Python for web development

Web development means
- Developing websites
- Developing REST-APIs
- Developing Microservices
"""

"""
We have many web frameworks in python
like

flask (Micro framework)
django (Bigger framework))
fastapi
many more
"""

"""
In our training, we will discuss flask-framework
"""

"""
Using flask-framework
1. Using flask-framework we can develop websites
2. Using flask-framework we can develop REST APIs
3. Using flask-framework we can develop microservices
"""

"""
We will discuss,
How to use flask-framework to create REST-API
"""

"""
Install flask:
pip install flask
"""

"""
Example to understand API:
    Suppose, we want to provide access to our database with others/public
    then
    how we can  provide access to our database with others/public ??
    
    ONE OPTION is we can create separate credentials with restricted permissions
    and we can share the credentials with others/public
    
    This option is very much limited, widely we can't use.
"""

"""
We got 2 solutions to provide access to our database with others/public
1. SOAP: Simple Object Access Protocol
2. REST: REpresentational State Transfer Protocol

Both are called Architectures/Designs/Styles
Both tells how we can provide access to our database with others/public

both tells to introduce some DOOR/GATE/INTERFACE between our-application with others/public
it is like
Our-DB/our-App  <--INTERFACE-->   others/public

This INTERFACE is also called as APPLICATION PROGRAMMING INTERFACE(API)

Both tells how to write such INTERFACE
"""

"""
REST came after SOAP
- REST is popular
- REST is easy implement and manage
"""

"""
flask/fastapi/django all are impletemented REST architecture
We just need to know how to use each framework to create REST-API
"""

"""
Assume, we need to provide COMPLETE-ACCESS/FULL-ACCESS to our DB/application

So, COMPLETE-ACCESS/FULL-ACCESS to our DB/application 
means

- Adding new record to our DB/application 
- Getting existing records from our DB/application 
- Updating existing records present in our DB/application
- Delete existing records present in our DB/application 
"""

"""
HTTP Methods: GET/POST/PUT/PATCH/DELETE

POST             - Adding new record to our DB/application 
GET               - Getting existing records from our DB/application 
PUT/PATCH     - Updating existing records present in our DB/application
DELETE          - Delete existing records present in our DB/application 
"""

"""
About web server
- flask has builtin web server, BUT we can use this server for development purposes
    We can't use it for production purposes.
- Few production web servers examples:
    https://wsgi.readthedocs.io/en/latest/servers.html
"""

# -----------
# Create App
##########


import flask
my_rest_api_app = flask.Flask("MyApiAppName")
#####################

# -----------
# END POINT -1 : URL http://127.0.0.1:5000/getdbdataapi mapped to route("/getdbdataapi")
##########
@my_rest_api_app.route("/getdbdataapi", methods=["GET"])
def getdbdataapi():
    import sqlite3
    my_db_connection = sqlite3.connect("mydatabase.db")
    cursor = my_db_connection.cursor()
    cursor.execute("SELECT * FROM MYTABLE")
    my_db_data = cursor.fetchall()
    my_db_connection.close()
    return flask.jsonify(my_db_data)
#####################


# -----------
# Run builtin server
##########
my_rest_api_app.run() # default host: 127.0.0.1, port=5000
#####################