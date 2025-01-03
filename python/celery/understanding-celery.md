The goal of this tutorial is to simplify enough concepts to unlock some roadblocks on a beginner's path to an overall understanding of task queues (such as Celery) and ease their exploration of more advanced features.

In my opinion, the first and most difficult hurdle for a newbie trying to understand a tool is to have an idea of the kind of problems it solves. What's its reason for existing? What were the problems that motivated its creation? A simple definition often isn't enough to address these questions satisfactorily.

Let's forgo a definition of what task queues are to rather just describe what they can do. We'll then go through some examples to illustrate why it would be a good thing. 

# The problem

When computer programs run they typically are restricted to only access variables, classes, functions, and other such references located within their respective scope. They cannot reach over to access memory assets located beyond their allotted spaces. Additionally since two running processes cannot have overlapping memory spaces it therefore stems that they would also not be able to share memory objects. The necessity sometimes arises however for separate applications to be able to interoperate at that level, or close. This is commonly known as Inter-process Communication or IPC. There are many solutions to IPC, task queues are but one.

To speak very broadly, task queues can help your programs communicate with each others. They offer a tool that allows applications to reach beyond the scope of their respective processes, programming language, or even physical constraints. This can be useful in a number of ways, for example when you want to break one heavy tasks to spread its load among multiple concurrent routines, said routines will be running in their own isolated space but will probably still need to communicate fast. Another useful application is when a program needs to access a function defined in another program running in a different process, a task queue can be set up so that these programs can talk to each other. A task queue can thus be described as a communication layer connecting a set of isolated processes into a network.

# Some more specific example use-cases
#### Offloading resource intensive operations away from one app onto another
That is, one of your apps "outsources" something too heavy, slow, or out of place to another process outside of it. That external process could be another app, but could also simply be a second instance of the same app just running for the specific purpose of dealing with these heavy tasks. As an example, consider the file processing in your image resizing web service. A client of your app just uploaded a file, it now needs to be resized and compressed. You could have the user wait for the processing to end before responding to the request, but it seems inefficient and unecessary. What if your server application could just offload specifically the image processing part of that request to an external application and be on its way, returning quickly with a response that contains an url that the client can then poll to get a status on the ongoing resizing operation. 

#### Microservices
If you've never heard of them, they consist in an infrastructure made of a number of somewhat minimal, highly specialized, and isolated services, that form the supporting framework of a more complete application (or set of applications). Like any other architecture style there are some advantages (and inconvenients) in developing with this approach. You can read more about it here [1] (Martin Fowler's article on Microservices). Where does a task queue come in? Microservices tend to be insulated from each other, running as standalone applications, but it may happen that one service depends on functionalities present in another, so there needs to be a (reasonably fast) way for them to communicate and invoke each other's API.

#### Concurrency
Processing a set of operations concurrently that would otherwise be processed contiguously. Imagine the following scenario, you've been called in to improve the performance of a web admin panel. Its users have been complaining that whenever they update some contents it can take between 5 to 10 seconds to get a response from the server. You investigate and realize that the main bottleneck is that when the data is updated it sometimes affects a number of resources that need to have their cache refreshed, and this is currently done one resource at a time, one after the other. Admittedly this could be a sign of bad design, but you can't do much about it at the moment. You realize that instead of regenerating the cache stores sequentially it would probably speed things up considerably if the refresh of each cache was delegated to an external copy of the running app. A number of such copies working concurrently would in theory noticeably reduce the latency. So you create five copies of the main app with the sole purpose of using their cache refreshing functions and you set up a task queue and register these copies as listeners. Whenever a resource needs its cache refreshed the main app simply publishes in the queue all the necessary data to find the resource and moves on. Whichever of its copies is idle grabs the item at the top of the queue and gets to work. The result is that your end users experience a noticeable speed up of their application.

#### Scheduled tasks
Imagine wanting to perform certain tasks according to a schedule. There are some utilities present in Unix such as cron that already afford you a certain level of capabilities to do such things. But cron is still just a rather simple tool with a limited vocabulary, by itself it doesn't afford you the flexibility of a programming language. With the ability to communicate across processes, you could create schedulers capable of invoking operations exposed by other apps through some IPC layer such as Celery. With the full force of a programming language like Python, it could be made as simple or complex, specialized or general as you want. Consider a utility that pings your API every 10 seconds and sends you a text message when it doesn't get a response after 5 pings.

--- 

By now you should probably have an idea of the potential task queues bring to your toolset.

Here's an overview of how a tool like that would be set up. I use a descriptive terminology to illustrate what's going on. We'll introduce the jargon once the concept is understood. This is a broad oversimplification. Implementations can be somewhat more involved, but I think this is enough to understand what's going on. Let's say you were to implement the first version of PMTQ (Poor Man's Task Queue), this is how things would probably look like at the beginning:
1. you have a program in which you've identified a number of functions that could be helpful to a bunch of other processes. You'd like to expose these to the outside world (outside of the application's running process).
2. you create a small utility within your app that has two specific purposes:
    -  i. it monitors an external file for entries that will indicate that certain functions should be called with certain parameters.
    - ii. it then calls these functions and clears the corresponding entry from the file.
3. That utility is called a *worker* and the file it's monitoring is the *message queue*. The worker now awaits messages coming in the queue...
4. Another app, a client app, is given the names and parameters of the remote functions (i.e. their signature), as well as the location of the queue file to send messages to when it needs some work done.
5. The client app posts a message to the queue with the name of a function and some parameters. It also signs its request by providing an ID.

    [imaginosaure_taskq.txt]

    --{
        "task_id": "45bc8d0ae7c9f8e810e8d",
        "function": "Image.resize",
        "params": {
            "file": "/tmp/ukz4e82wk.jpg",
            "width": 800,
            "height": 300,
            "x": 27,
            "y": 33
        }
    }--

6. The worker sees the message and recognizes one of its assigned functions and the provided parameters.
7. The worker executes the function with the parameters found as part of the message, then dumps the result in a results file, where it can be retrieved by whatever app requested it.

    [imaginosaure_results.txt]
    --{
        "task_id": "45bc8d0ae7c9f8e810e8d",
        "result": "/tmp/ukz4e82wk_800x300.jpg",
    }--

There you have a rudimentary task queue.

Celery
------

Now, a libray like Celery does all of this in such a clever way that it sometimes leaves beginners wondering "what the hell just happened?!?"

    ```
    # tasks.py
    from celery import Celery 

    app = Celery('tasks', broker='amqp://guest@localhost//')

    @app.task
    def zombocom():
        return "Welcome to ZomboCom. You can do anything at ZomboCom..."
    ```
     
In the code above you have the necessary for both (1) running a worker process that will register the task and call upon it when needed and (2) creating a client process of the same app that can delegate the task to the previously started worker. Which is which all depends on how you start the process.

Let's first run the worker's instance. We do this with the `celery` command line utility provided by your platform or virtualenv and its `worker` argument:

    $ celery worker -A tasks --loglevel=info

    - the `-A tasks` or `--app tasks` is the option where we specify the module (tasks.py without the extension). By default it looks for an instance of Celery named `app` or `celery` within the module. This can be explicitly specified like this `-A tasks:app`. I encourage you to be explicit and use this form, even if you name your celery app 'celery' or 'app', it takes but an extra second when writing, but keeps everything clear. So
    
    -- $ celery worker -A tasks --loglevel=info
    ++ $ celery worker -A tasks:app --loglevel=info
    
    - the `--loglevel` is self explanatory (if not check the documentation)


