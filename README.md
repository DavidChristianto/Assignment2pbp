# PBP Django Project Template

Platform-Based Programming (CSGE602022) - Organized by the Faculty of Computer Science Universitas Indonesia, Odd Semester 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

[Hyperlink] https://assignment2pbp.herokuapp.com/katalog/

[Hyperlink] https://assignment2pbp.herokuapp.com/mywatchlist/

# Assignment 2 Question

#### 1. Create a diagram containing client request to the Django web application and its response. Also explain the flow of the diagram and how the urls.py, views.py, models.py and HTML files connected each other.
#### Answer: 
<img width="784" alt="Screen Shot 2022-09-14 at 14 45 17" src="https://user-images.githubusercontent.com/88826287/190093495-ab803c6e-0a2d-4e0d-a75b-6c5e8c9e0286.png">

   
   Django MVT architecture consist of 3 parts: 
   1. M (Model)      : the data access layer
   2. T (Template)   : the presentation layer
   3. V (View)       : the business logic layer, the bridge between models and templates.
   
   The explaination about the diagram
   1. The user sends a request to the Django platform.
   2. urls.py sends a request object to views.py and processed as a function call.
   3. if the request involves a database, then the view component, i.e. view.py will request the required data from the model component, i.e. model.py,         which data will be returned to views.py and will be displayed as webpage.
   4. If not involving database, views.py will retrieve the HTML template which will be displayed as a webpage.
   5. The next step, the data from views.py will be transferred to the template
   6. Then, the response will be processed and generated in the form of HTML webpage
   
#### 2. Explain why do we use virtual environments? Let's say, if we do not use the virtual environments, can we still create a Django web application?
#### Answer:
   In my opinion, the answer to the question if we do not use the virtual environments, can we still create a Django web application? is possible, but it    is still recommended to use virtual environments in creating Django web applications. if we don't use it, it will most likely cause a crash if we do      the wrong installation of the required package. virtual environment there is a tool that allows us to separate the projects that we create into their      own isolated scope. To put it another way, virtual environments aid in dependency management by isolating projects from one another. This virtual          environment is typically used when we have multiple projects or create a new project to ensure that the version of a library used in one project does      not change if we update the same library in another project. In other words, when you update a system dependency, some of your projects that rely on      that dependency may no longer be relevant to the newer version, resulting in errors.


#### 3. Explain how did you implement the steps on point 1 to point 4 above.
#### Answer:
   1. In the first point, the function created in views.py serves to accept the request object as an argument, this function is also responsible for             creating a dictionary that contains a Queryset(from model.py) that will return the render function (render()). This render function has 3 arguments,       namely the request object as the first argument, HTML template as the second argument and the dictionary as the third argument(this dictionary will       contain the items contained in the json file).
   2. url.py will map the path to the appropriate function in views.py because view.py will return the render function. The render() function is                 responsible for mapping to databases and HTML files.
   3. The data returned to views.py will be used as arguments to the render function. This render function outputs an HttpResponse object
   4. What is done in deploying to Heroku is to create a new app first, then also create a Procfile, dpl.yml, and .gitignore, then do configurations in       settings.py. then the next step is to add the API key and name that is on Heroku to github by creating a secrets repository. then the last thing         is to re-run all jobs on the action menu on github and wait until the deployment is complete

# ============================== Assignment 3 ==============================
# Postman Sreenshots
1. XML URL using postman
![postman1](https://user-images.githubusercontent.com/88826287/191458815-e06e51b5-953a-4ea9-9267-45d590bc14a7.jpg)

2. JSON URL using postman 
![postman2](https://user-images.githubusercontent.com/88826287/191458956-15641d16-e77e-4e25-9320-230a3f8c337d.jpg)

3. HTML URL using postman
![postman3](https://user-images.githubusercontent.com/88826287/191459873-76d80075-79da-4b5c-b554-ce03b3acf77a.jpg)

# Assignment 3 Question
## 1. Explain the difference between JSON, XML, and HTML!
The difference between HTML, XML, and JSON can be seen from 3 things, namely the content, the structure used, and the formatting. The first attempt to combine these editing problems into a single process was the development of GML in the 1960s by IBM employees. The way GML tries to solve this problem is to wrap the tag around the content that contains the instructions in it to define the structure and formatting of the content inside the tag. These tags will also have the ability to be nested (tags within tags) to have more control over the content. But as more and more people get involved and use SGML (the standard version of GML), this makes GML even more difficult to use. This mimics html development, where the HTML will wrap the content in tags. However the rules regarding which tags can be used when and where are much stricter, which can affect the structure of the information within them. Because of these structural problems, XML was developed. XML will try to address this issue head-on by maintaining all the strict rules of SGML, therefore preserving the structure of the information (just like a database), without worrying about formatting at all (this is left to HTML to handle). This will also address another issue which is an increase in the amount of content available. XML will be the format for sending and receiving the records and HTML will be responsible for formatting and displaying the records that are called. JSON (JavaScript Object Notation) is a lightweight and completely language-independent data exchange format. It is based on the JavaScript programming language and is easy to understand and generate.

so, the conclusion about the difference between HTML and XML and JSON is: 
1. HTML is responsible for displaying and formatting data, whereas XML and JSON is responsible for sending and receiving data.
2. JSON is JavaScript Object Notation, whereas XML is Extensible markup language
3. JSON is based on JavaScript language, whereas XML is derived from SGML
4. JSON does not support namespaces, but support array. Whreas XML support namespaces, but does not support array.

## 2. Explain why we need the data delivery in implementing a platform.
The concept of data delivery is sending data from one location to another using methods and formatting. In this era of digitization, most of them have databases that can accommodate very large amounts and sizes of data. With this situation, data delivery becomes very important, especially in implementing the platform, because only when the user requests the required data, then the application will retrieve the requested data from the database (not all data) and present it to the user. So this will reduce the storage load that will burden the system device.

So the conclusion is that with data delivery, an application or platform that is used does not need to store data on itself so that it does not burden the storage system

## 3. Explain how you can implement the checklists above.
1. First of all run "python manage.py startapp mywatchlist" on the terminal (on the directory of my local repository) to create a new app. 
2. write "urls.py" to the application to add the mywatchlist URL path, so it can be accessed via http://localhost:8000/mywatchlist or by running the command python3 manage.py runserver on the local terminal.
3. Add class item "mywatchlist" in the models.py, with 5 attributes: watched, title, rating, release date, and review.
4. Make initial_mywatch_data.json file inside of a folder "fixtures" that contain data for that webpage, which are 10 movies.
5. Added multiple functions in "views.py" that allowed the data to be represented via XML, HTML, and JSON. The functions also be added in the 'urlpatterns' list found in "urls.py"
6. After that, edit the Procfile so it would migrate the models and load the data(JSON file) when it deployed. 
7. Lastly, pushed the local repository onto GitHub(add, commit, push), and it automatically deployed in Heroku.

# ========================= ASSIGNMENT 4 =========================
## QUESTION 1 : What does {% csrf_token %} do in the <form> element? What happens if there is no such "code snippet" in the <form> element?
#ANSWER:
CSRF stands for Cross-Site Request Forgery which is also often referred to as XSRF, or adversarial linking. CSRF itself is an attack that makes internet users unknowingly send a request to the website through the website app that is being used. So the CSRF code token used on the form is a token that is used to prevent CSRF attacks, where usually attacks that occur will harm and hijack user sessions. The simple mechanism of this CSRF token is
make this token as "Key" which will be matched between request from user and current session, if match will be accepted and if not match will be rejected. Therefore, in the Django platform we can generate this CSRF token using the get_token() function to encode the real CSRF token so that it cannot be seen by other sites or websites. then what will happen if you don't use this token? Generally Django will raise a 403 (CSRF verification failed) error because this is the default in settings.py which will be automatically activated, besides if you don't have this token, CSRF attacks can easily occur when unauthorized users fake requests and gain access from authorized users.
 
##QUESTION 2 : Can we create the <form> element manually (without using a generator like {{ form.as_table }})? Explain generally how to create <form> manually.
#ANSWER:
in my opinion it is possible to create form elements manually. the simple mechanism is that we can use a form tag and wrap the temporary input (it also contains the URL it points to). Then close the form tag.
   
##QUESTION 3 : Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.

##ANSWER: 
The user makes a request which will be read in urls.py, then views.py will run the create_task function to create and save the data. After that the process will be directed to the show_todolist function where the new data that the user just created is already in the database so that the render function can use the new data and provide a response in the form of output in the form of html to the user.
   
##QUESTION 4 : Explain how you implement the checklist above.
#ANSWER:
1. First of all run "python manage.py startapp todolist" on the terminal (on the directory of my local repository) to create a new app. 
2. write "urls.py" to the application to add the todolist URL path, so it can be accessed via http://localhost:8000/mywatchlist or by running the command python3 manage.py runserver on the local terminal.
3. Add class item "Task" in the models.py, with 5 attributes: user, date, title, description, is_finish
4. Make login.html, register.html, todolist.html, and create_task.html
5. Added multiple functions in "views.py" (login_user, logout_user, create_task, update_task_status, remove_task) The functions also be added in the 'urlpatterns' list found in "urls.py"
6. After that, edit the Procfile so it would migrate the models and load the data(JSON file) when it deployed. 
7. Lastly, run command python3 manage.py makemigrations and migrate, also pushed the local repository onto GitHub(add, commit, push), and it automatically deployed in Heroku.


## Introduction

This repository is a template that is designed to help students who take the Platform-Based Development/Programming Course (CSGE602022) to know the structure of a Django Web application project, including the files and configurations that are important in running the application. You can freely copy the contents of this repository or utilise this repository as a learning material and also as a starting code to build a Django Web application project.

## How to Use

If you want to use the code template in this repository as a starter code for
developing a Django Web application:

1. Open the GitHub page of the code template repository and click "**Use this template**"
   button to make a copy of the repository into your own GitHub account.
2. Clone the new Django template repository from your GitHub account to a
   location in the filesystem of your local development environment by using
   Git:

   ```shell
   git clone <URL to your repository on GitHub> <path in local development environment>
   ```
3. Go to the location where the cloned repository is located in the local
   development environment:

   ```shell
   cd <path to the cloned repository>
   ```
4. Create a Python virtual environment named `env` inside the cloned repository
   by using Python's `venv` module:

   ```shell
   python -m venv env
   ```
5. Activate the virtual environment:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```
6. Verify the virtual environment has been activated by looking at the prompt
   of your shell. Make sure there is a `env` prefix in your shell. For example:

   ```shell
   # Windows using `pwsh` shell
   (env) PS C:\Users\RickeyAstley\my-django-app
   # Linux/Unix, e.g. Ubuntu using `bash` shell
   (env) rickeyastley@ubuntu:~/my-django-app
   ```

   > Note: You can use [Visual Studio Code][] (with Python extension) or [PyCharm][]
   > to open the source code directory that has a virtual environment directory.
   > Both will detect the virtual environment and use the correct Python virtual
   > environment. Furthermore, you can also run your shell directly in both text
   > editor/IDE.
7. Install the dependencies needed to build, test, and run the application:

   ```shell
   pip install -r requirements.txt
   ```
8. Run the Django Web application using local development server:

   ```shell
   python manage.py runserver
   ```
9. Open http://localhost:8000 in your favourite Web browser to see if the Web
   application is running.

## Deployment Example

The code template provided a GitHub workflow to deploy the sample Django Web
application to [Heroku][], which is a Platform-as-a-Service (PaaS) provider
that lets you to build and run a Web application on their infrastructure. You
can read the instructions at [Tutorial 0][] to figure out how to configure the
GitHub Actions to run the provided workflow in your repository.

For reference, the deployed Django Web application example from the original
code template repository can be found at: https://django-pbp-template.herokuapp.com.

## Next Actions

If you have successfully created your own repository and set up the Django Web
application project, you can start working on the weekly tutorials and assignments
related to Django Web application development. 

If you found any issues or have ideas to improve the code template, feel free
to discuss your proposal via the [issue tracker](https://github.com/pbp-fasilkom-ui/django-pbp-template/issues)
and create a Pull Request (PR) containing your changes to the code template.

## Credits

This template was based on [PBP Odd Term 2021/2022](https://gitlab.com/PBP-2021/pbp-lab) written by 2021 Platform Based Programming Teaching Team ([@prakashdivyy](https://gitlab.com/prakashdivyy)) and [django-template-heroku](https://github.com/laymonage/django-template-heroku) written by [@laymonage, et al.](https://github.com/laymonage). This template is designed in such a way so that students can use this template as a starter and reference in doing assignments and their work.

[Heroku]: https://www.heroku.com/
[Tutorial 0]: https://pbp-fasilkom-ui.github.io/ganjil-2023/en/assignments/tutorial/tutorial-0
[Visual Studio Code]: https://code.visualstudio.com/
[PyCharm]: https://www.jetbrains.com/pycharm/


