source: https://gabrieltanner.org/blog/docker-compose/

- Compose allows you to manage multiple Docker containers by specifying rules from a single file.

## Basic structure of the Compose file
- The file may be named `compose.yml` or `docker-compose.yml`.
- 5 top-level sections are commonly used in practice, in addition to the optional `version` and `name` declarations (1 which is deprecated, 2.x, or 3.x):
    - `services`: to declare the various applicative containers (e.g. app, database, web server, caching utilities, etc)
    - `volumes`:  a dedicated section to declare shared storage spaces.
    - `networks`: to declare the networks used by services to communicate.
    - `configs`: #TODO
    - `secrets`: #TODO

#TODO

A sample file could look like this:

    services:
      db:
        image: mysql:5.7
        volumes:
          - db_data:/var/lib/mysql
        restart: always
        environment:
          MYSQL_ROOT_PASSWORD: somewordpress
          MYSQL_DATABASE: wordpress
          MYSQL_USER: wordpress
          MYSQL_PASSWORD: wordpress

      wordpress:
        depends_on:
          - db
        image: wordpress:latest
        ports:
          - "8000:80"
        restart: always
        environment:
          WORDPRESS_DB_HOST: db:3306
          WORDPRESS_DB_USER: wordpress
          WORDPRESS_DB_PASSWORD: wordpress
          WORDPRESS_DB_NAME: wordpress

    volumes:
      db_data: {}


## Concepts / Keywords #TODO

The core aspects of the Compose file are its concepts which allow it to manage and create a network of containers. In this section, we will explore these concepts in detail and take a look at how we can use them to customize our Compose configuration.

### Services

The services tag contains all the containers which are included in the Compose file and acts as their parent tag.

    services:
      proxy:
        build: ./proxy
      app:
        build: ./app
      db:
        image: postgres

Here you can see that the services tag contains all the containers of the Compose configuration.

### Base image (Build) #TODO

The base image of a container can be defined by either using a preexisting image that is available on DockerHub or by building images using a Dockerfile.

Here are some basic examples:

    services:
      alpine:
        image: alpine:latest
        stdin_open: true
        tty: true
        command: sh

Here we use a predefined image from DockerHub using the image tag.

    services:
      app:
        container_name: website
        restart: always
        build: .
        ports:
          - '3000:3000'
      command:
        - 'npm run start'

In this example, we define our images using the build tag which takes the destination of our Dockerfile as a parameter.

The last option of defining the base image is to use a Dockerfile with a custom name.

    build:
      context: ./dir
      dockerfile: Dockerfile.dev

### Ports #TODO

Exposing the ports in Compose works similarly as in the Dockerfile. We differentiate between two different methods of exposing the port:

Exposing the port to linked services:

    expose:
     - "3000"
     - "8000"

Here we publish the ports to the linked services of the container and not to the host system.

Exposing the port to the host system:

    ports:
      - "8000:80"  # host:container

In this example, we define which port we want to expose and the host port it should be exposed to.

You can also define the port protocol which can either be UDP or TCP:

    ports:
      - "8000:80/udp"

### Commands #TODO

Commands are used to execute actions once the container is started and act as a replacement for the `CMD` action in your Dockerfile.

The `CMD` action is the first command that gets executed when the container is started and is therefore mostly used to start a process e.g. start your website through a CLI command like `npm run start`.

    app:
      container_name: website
      restart: always
      build: ./
      ports:
        - '3000:3000'
      command:
        - 'npm run start'

Here we create a service for a website and add the starting command using the command tag. This command will be executed after the container has started and will then start the website.

For more information about `CMD`, `RUN`, and `Entrypoint` you can read this article which discusses the details and compares their functionality.

### Volumes #TODO

Volumes are Docker’s preferred way of persisting data which is generated and used by Docker containers. They are completely managed by Docker and can be used to share data between containers and the Host system.

They do not increase the size of the containers using it, and their context is independent of the lifecycle of the given container. [Docker volumes](https://docs.docker.com/storage/volumes/)

There are multiple types of volumes you can use in Docker. They can all be defined using the volumes keyword but have some minor differences which we will talk about now.

##### Normal Volume:

The normal way to use volumes is by just defining a specific path and let the Engine create a volume for it. This can be done like this:

    app:
      volumes:
        # Just specify a path and let the Engine create a volume
        - /var/lib/mysql

##### Host path binding:
- less recommended than Docker volumes as bindings are not manageable by Docker.

    app:
      volumes:
        - /opt/data:/var/lib/mysql

##### Named volume:

Another type of volume is the named volume which is similar do the other volumes but has its own specific name that makes it easier to use on multiple containers. That’s why it’s often used to share data between multiple containers and services.

    services:
      app:
        volumes:
          - datavolume:/var/lib/mysql

    volumes:
      datavolume: {}

##### Dependencies:

- the `depends_on` declaration ensures the sequence in which services are started.

    services:
      ghost:
        container_name: ghost
        restart: always
        image: ghost
        ports:
          - 2368:2368
        environment:
          - .
        depends_on: [db]
       db:
         image: mysql
         command: --default-authentication-plugin=mysql_native_password
         restart: always
         environment:
           MYSQL_ROOT_PASSWORD: example

- here the `ghost` service declares that it requires the MySQL database to work.

##### Environment variables:
It's usually recommendable to decouple your application from its configuration (see The 12-Factor App). This can be achieved by setting the configurations in the environment the application is running in instead and then pull the configuration from there.

Compose allows you to set configuration in the environment in a variety of approaches:

- The `environment` attribute lets you explicitly set variables:
    - using the `key=value` form (similar to using the `--environment|-e` flag with `docker container run`).
    ```
    services:
      web:
        environment:
          - ENABLE_LOGGING=1
          - ADMIN_EMAIL=admin@example.com
    ```
    - or by seamlessly passing variables from the Compose environment to the container, by simply naming them.
    ```
    services:
      web:
        environment:
          - ENABLE_LOGGING
          - ADMIN_EMAIL
    ```
- The `env_file` attribute lets you specify external files containing variable declarations (e.g. `.env`)

    services:
      web:
        env_file:
          - variables.env

- #TODO : secrets

#### Networking #TODO
- Networks define communication rules between containers, as well as between containers and host system.
- They can be configured to insulate communication, allowing for more secure applications.
- Compose sets up a default network any of the containers defined in the Compose file can communicate through.
- Containers joining the default network are reachable by other containers on the network, and are also discoverable by the hostname defined in the Compose file.

##### Specify custom networks:
The `networks` top-level section lets you set your own networks, along with additional drivers and options.

    networks:
      frontend:
      backend:
        driver: custom-driver
        driver_opts:
          foo: "1"

The service's `networks` attribute lets you specify which networks it registers to.

    services:
      proxy:
        build: ./proxy
        networks:
          - frontend
      app:
        build: ./app
        networks:
          - frontend
          - backend
      db:
        image: postgres
        networks:
          - backend

    networks:
      - frontend
      - backend

- Full list of the network configuration options: #TODO
[Top-level `networks`](https://docs.docker.com/compose/compose-file/06-networks/)
[Service-level `networks` attribute](https://docs.docker.com/compose/compose-file/05-services/#networks)

##### External (Pre-existing) networks: #TODO

You can use pre-existing networks with Docker Compose using the external option.

    networks:
      default:
        external:
          name: pre-existing-network

In this example, Docker never creates the default network and just uses the pre-existing network defined in the external tag.

##### Configure the default networks:
An alternative to defining an additional network is to simply reset options on the default network.

    version: "3"

    networks:
      default:
        driver: custom-driver

##### Linking containers:
- a service's `links` attribute lets you set additional aliases other services can be reached from within.
- They're not required to enable services to communicate.
- By default, any service can reach any other service at that service's name.

    services:
      web:
        build: .
        links:
          # the service can reach db using either "db" or "database".
          - "db:database"
      db:
        image: postgres


### CLI #TODO
All the functionality of Docker-Compose is executed through its build in CLI, which has a very similar set of commands to what is offered by Docker.

    build    Build or rebuild services
    help     Get help on a command
    kill     Kill containers
    logs     View output from containers
    port     Print the public port for a port binding
    ps       List containers
    pull     Pulls service images
    rm       Remove stopped containers
    run      Run a one-off command
    scale    Set number of containers for a service
    start    Start services
    stop     Stop services
    restart  Restart services
    up       Create and start containers
    down     Stops and removes containers

They are not only similar but also behave like their Docker counterparts. The only difference is that they affect the entire multi-container architecture which is defined in the docker-compose.yml file instead of a single container.

Some Docker commands are not available anymore and have been replaced with other commands that make more sense in the context of a completely multi-container setup.

The most important new commands include the following:

    docker-compose up
    docker-compose down

### Using Multiple Docker Compose Files
- Using multiple Compose files lets you set up a Compose application for different environments or workflows.
- This is useful for large applications that may use dozens of containers, with ownership distributed across multiple teams.
- For example, if your organization or team uses a monorepo, each team may have their own “local” Compose file to run a subset of the application.
- They then need to rely on other teams to provide a reference Compose file that defines the expected way to run their own subset.
- Complexity moves from the code into the infrastructure and the configuration file.

##### Merging Compose files with the `-f` flag
- The quickest way to work with multiple Compose files.
- Merging rules means this can soon get quite complicated.

Docker Compose provides two other options to manage this complexity when working with multiple Compose files. Depending on your project's needs, you can:

##### Extend a Compose file by referring to another Compose file and selecting the bits you want to use in your own application, with the ability to override some attributes.
##### Include other Compose files directly in your Compose file.

### Compose in production

Docker Compose allows for easy deployment because you can deploy your whole configuration on a single server. If you want to scale your app, you can run it on a Swarm cluster.

There are still things you probably need to change before deploying your app configuration to production. These changes include:

    Binding different ports to the host
    Specifying a restart policy like restart: always to avoid downtime of your container
    Adding extra services such as a logger
    Removing any unneeded volume bindings for application code

After you have taken these steps you can deploy your changes using the following commands:

docker-compose build
docker-compose up --no-deps -d

This first rebuilds the images of the services defined in the compose file and then recreates the services.
Example

Now that we have gone through the theory of Compose let’s see some of the magic we just talked about in action. For that, we are going to build a simple Node.js application with a Vue.js frontend which we will deploy using the tools we learned about earlier.

Let’s get started by cloning the repository with the finished Todo list application, so we can directly jump into the Docker part.

git clone --single-branch --branch withoutDocker https://github.com/TannerGabriel/docker-node-mongodb.git

This should give you a project with the following folder structure:

Docker Project folder structure

Now that we have the project setup lets continue by writing our first Dockerfile for the Node.js backend.

FROM node:latest

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./

RUN npm install

# Bundle app source
COPY . .

EXPOSE 3000:3000
CMD [ "node", "server.js" ]

All right, let’s understand what’s going on here by walking through the code:

    First, we define the base image using the FROM keyword
    Then we set the directory we are going to work in and copy our local package.json file into the container
    After that, we install the needed dependencies from the package.json file and expose the port 3000 to the host machine
    The CMD keyword lets you define the command which will be executed after the container startup. In this case, we use it to start our express server using the node server.js command.

Now that we have finished the Dockerfile of the backend lets complete the same process for the frontend.

FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./
COPY .env ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]

This file is similar to the last one but installs an HTTP server which displays the static site we get when building a Vue.js application. I will not go into further detail about this script because it isn’t in the scope of this tutorial.

With the Dockerfiles in place, we can go ahead and write the docker-compose.yml file we learned so much about.

First, we define the version of our Compose file (in this case version 3)

version: '3'

After that, we start defining the services we need for the project to work.

services:
    nodejs:
        build:
            context: ./backend/
            dockerfile: Dockerfile
        container_name: nodejs
        restart: always
        environment:
            - HOST=mongo
        ports:
            - '3000:3000'
        depends_on: [mongo]

The Node.js service uses the Dockerfile of the backend which we created above and publishes the port 3000 to the host machine. The service also depends on the mongo service which means that it lets the database start first before starting itself.

Next, we define a basic MongoDB service which uses the default image provided on DockerHub.

     mongo:
        container_name: mongo
        image: mongo
        ports:
            - '27017:27017'
        volumes:
            - ./data:/data/db

This service also publishes a port to the host system and saves the data of the database in a local folder using a volume.

The last service we need to define is the frontend which uses the frontend Dockerfile to build the image and publishes port 8080 to the host system.

    frontend:
        build:
            context: ./frontend/
            dockerfile: Dockerfile
        container_name: frontend
        restart: always
        ports:
            - '8080:8080'

That is it! We have finished our Docker files and can now move on to running the application. This is done using the following two commands:

# builds the images from the dockerfiles
docker-compose build

# starts the services defined in the docker-compose.yml file
# -d stands for detached
docker-compose up -d

As indicated by the terminal output, your services are now running and you are ready to visit the finished website on localhost:8080 which should look something like this:

Docker Node example

Now you can add todos to your list using the add button and your app should look like this.

Docker Node items example

If you reload the page the items should stay the same because they are saved in our database. The last thing I want to show is how you can get the debug logs of the running containers.

docker-compose logs

This command will display all logs of the running containers and can help you debug your errors or check the current state of your application.

That is it for the project. The source code for the whole project can be found on my Github.
Conclusion

You made it all the way until the end! I hope that this article helped you understand the Docker Compose and how you can use it to improve your development and deployment workflow as a developer.

If you have found this useful, please consider recommending and sharing it with other fellow developers. If you have any questions or feedback, let me know in the comments down below.
