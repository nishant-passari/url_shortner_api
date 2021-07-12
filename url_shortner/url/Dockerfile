# Base image to be used
FROM python:3.6

# Setting the environment variable
ENV PYTHONUNBUFFERED 1

# Copy the requirements.txt file to the working dir
COPY url_shortner/requirements.txt /testapi/

# Copy the current directory contents into the container at /testapi/
COPY url_shortner/ /testapi/

# Setting up the working directory
WORKDIR /testapi

# Install the requirements
RUN pip3 install -r requirements.txt

# Port from the container to expose to host
EXPOSE 8000

# Tell image what to do when it starts as a container
CMD /testapi/start.sh
