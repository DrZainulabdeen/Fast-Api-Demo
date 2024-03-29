# Fast-Api-Demo

This is the demo of using FastAPI and creating a service which takes an input as a json object and returns the name. 

## Getting started

To get started you need to install fastapi, uvicorn and pydantic. Just copy the command and run it in your terminal.

```
pip install fastapi uvicorn pydantic

```

Then you can fork this project and run `Main.py`

You can run using the command 

```
uvicorn Main:app --reload

```

Here we are using ´uvicorn´ to run the project and `Main` is the name of our python file and `app` is the instance of fastapi which we have defined in our code as:

```python

app = FastAPI()

```

This can be run without using `--reload` but using this provides our api the ability to reload whenever something changes in our app, so you dont need to run the app again.

To deploy it on a server use this command:

```
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
```

Make sure to have `all trafic` allowed in inbound rules in security groups for `ìpv4`


