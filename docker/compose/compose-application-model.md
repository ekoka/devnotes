- services: single instance of a running container image and configuration.
- networks: abstraction to allow services to communicate.
- volumes: service persistence layer.
- configs: used for platform or runtime dependent configuration data.
- secret: a specific type of configuration data for sensitive information.

- name: used to group resources together and isolate them from other applications or other installation of the same compose-specified application with distinct parameters. If creating resources on a platform, you must prefix resource names by project and set the label `com.docker.compose.project`.
