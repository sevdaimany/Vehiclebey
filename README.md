
# advertisement Service

This is a project for the cloud computing course, trying to use cloud 
services to create an app.
This app takes a text, image URL, and email and creates an advertisement 
if the image is in the vehicle category.

## Cloud Services

 - [Aiven cloud database](https://aiven.io/)
 - [Arvancloud Object 
Storage](https://www.arvancloud.com/en/products/cloud-storage)
 - [CloudAMQP RabbitMQ](https://www.cloudamqp.com/)
 - [Imagga Image Tagging](https://imagga.com/)
 - [Mailgun email delivery](https://www.mailgun.com/)




## Project architecture

![App 
Screenshot](https://github.com/sevdaimany/Vehiclebey/blob/master/photos/architecture.png)

## Installation

For deploying this project, you have to first set up a flask server.


* Installing Flask

```bash
$ pip install Flask
```

* installing other required packages

```bash
$ pip install postgres
$ pip install pika
$ pip install boto3
$ pip install logging
$ pip install botocore
$ pip install requests

```

## Screenshots

![App 
Screenshot](https://github.com/sevdaimany/Vehiclebey/blob/master/photos/request.png)
![App 
Screenshot](https://github.com/sevdaimany/Vehiclebey/blob/master/photos/showad.png)


