#creating a Dockerfile for the python application
FROM python:3.9

#setting the working directory of the python container
WORKDIR /user/src/app

#copying the python scripts to the working directory
COPY ./APIsalesdb.py /user/src/app/
COPY ./APIdw.py /user/src/app/

#installing necessary python packages
#so that the packages exist inside the python container instance
RUN pip install --upgrade pip && \
    pip install mysql-connector-python && \
    #the original swapi-python package had an error where
    #the BASE_URL in the setting.py was set to http://swapi.co/api
    #instead of http://swapi.dev/api as .co is no longer maintained or accessible
    #(as a result, I forked the original project to my github repository
    #and pointed the Dockerfile to install the 'revised'/'working' version
    #of the swapi-python package from my github path)
    pip install -e git+https://github.com/brianskim25/swapi-python@master#egg=swapi