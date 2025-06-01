# redis-and-python-integration

## Requirements

* python
* docker

## How to use

In the terminal run

```pip install virtualenv```

```virtualenv venv```

If you use Windows:
 ``` .\venv\Scripts\activate```

If you use Linux/WSL:
  ```Source venv/bin/activate```

With the virtual environment activated

```pip install -r requirements.txt```

Open another terminal tab and run the docker containers

```docker compose up -d```

Back to the previous terminal tab to run the python script

```python main.py```

##

To access the RedisInsight
```localhost:5540```

To add the database in the RedisInsight 
```redis://default@redis:6379```
