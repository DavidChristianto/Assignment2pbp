# ========================= ASSIGNMENT 6 =========================

## 1. Describe the difference between asynchronous programming with synchronous programming.

## Answer
The difference between synchronous and asynchronous is in the way tasks are executed. Sync performs its tasks one at a time, and can continue to run the next task if the previous task has been completed. Because of that the user has to wait for the data to load before doing anything. Whereas Asynchronous can run tasks in parallel and independently meaning that when the user makes a request, the data will be downloaded in the background so that the user does not have to wait for the data. In addition, Asynchronous is capable of sending multiple requests to the server (non-Blocking).

## 2. When Implementing Javascript and AJAX, there is an application in the paradigms of Event-Driven Programming. Describe the reasoning for those paradigms and state some examples of its application.

## Answer
Event driven programming is a programming paradigm in which the program flow is driven by user events such as mouse clicks, text input, sensor output, and messages passing from other programs or threads. Event-driven programming is the dominant paradigm used in graphical user interfaces and other applications (e.g., JavaScript web applications) that are centered on performing certain actions in response to user input. This is also true of programming for device drivers. An example of this is when user clicks "delete task" button then it will route to the appropriate function

## 3. Describe the implementation of asynchronous programming in AJAX.

## Answer
Add script to base.html.
Add  tag inside your body of HTML.
Write ajax JQuery syntax inside your script
Ajax will listen the event listener you write in script to perform the action you want.
That action and response/data will be processed asynchronously in the server.
The data will be shown in the page without needing to refresh.
   
## 4. Explain how you would implement the checklist above.

## Answer 
1. Add java scrip tag into base.html
2. edit views.py
3. Add path into urls.py
4. Add a GET function in todolist.html
5. Create the modal with bootstrap
6. Add POST function in todolist.html
7. Add, commit, and push the code onto GitHub
