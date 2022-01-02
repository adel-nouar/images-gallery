FROM python:3.9

# Where all the files will be copied and executed, if we don't specified,
# it'll copy everything in the / of the container (NOT a good practice to not specify)
WORKDIR /app

# The port number
EXPOSE 5050

# It'll copy all those file into /app (the local working directory WORKDIR)
COPY Pipfile Pipfile.lock ./

# It'll install all needed things and generate requirements.txt
RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

# It'll copy all files in WORDIR
COPY . ./

# The command that'll be executed -> "python main.py"
CMD ["python", "main.py"]