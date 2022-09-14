# PBP Django Project Template

Platform-Based Programming (CSGE602022) - Organized by the Faculty of Computer Science Universitas Indonesia, Odd Semester 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

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
   4. What is done in deploying to Heroku is to create a new app first, then also create a Procfile, dpl.yml, and .gitignore, then do configurations in         settings.py. then the next step is to add the API key and name that is on Heroku to github by creating a secrets repository. then the last thing is       to re-run all jobs on the action menu on github and wait until the deployment is complete
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
