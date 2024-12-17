# GSÜ Example
# Description

In this project, we will use a basic streamlit application for the front-end, a fastapi application for the back-end, and Kafka as the intermediary for communication. By taking values from the user via streamlit, we will send them to a topic named `to_process` in Kafka. Our back-end fastapi service will retrieve these values from the topic, perform the prediction process, and then write the processed result to the `processed` topic. In our consumer script, which we call a Python code, these values will be written into a JSON file. The streamlit application will continuously read the values from the JSON file and return the results to the user.

We will also monitor Kafka topics, producers, and consumers using an application named `kafkaui`.

Note: This system does not represent the best architecture for such an application; it was developed for teaching these technologies to students.

Diagram of the application workflow:
![Aarch](pictures/app-arch-basic.png "Arch")

# Deploying on AWS
- To deploy the application on AWS, first, a machine with **1GB RAM and 1VCPU** must be launched via the [AWS EC2](https://us-east-1.console.aws.amazon.com/ec2/) service. The **t2.micro** machine type can be chosen as it is free.
- During configuration, in the **security group** settings, access to all ports (not recommended) or only the port where the streamlit application will be published must be allowed.
- After launching the machine, access can be gained using SSH or EC2 Serial Console.
- Amazon machines likely come pre-installed with Python3. If not, you can refer to how to install Python on Debian/Linux machines.
- Install `git` on the machine to pull the necessary code.


### Installing Required Libraries
```
# If sudo privileges are not acquired, use sudo su to gain permissions.
yum install docker git -y

# Start the Docker service
systemctl restart docker
```

### Installing Docker Compose
To install Docker Compose, use the following commands:
```
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose version
```

### Execution
For the first execution, use the `--build` command to build the images.
```
docker-compose up --build
```

Then, access the application on port 8501 of the machine's public IP. Kafka information can be accessed via the KafkaUI application on port 8080.

Application Screenshots

- KafkaUI
  - ![Aarch](pictures/kafkaui.png "Arch")
- Streamlit
  - ![Aarch](pictures/streamlit-app.png "Arch") 
- FastAPI
  - ![Aarch](pictures/fastapi-app.png "Arch")
