FROM "python3.8"

COPY . /src 

COPY ../requirements.txt /src/requirements.txt

COPY ./templates src/templates

COPY ./static src/static 

WORKDIR /src 

RUN pip install -r requirements.txt

CMD ["python", "main.py"]