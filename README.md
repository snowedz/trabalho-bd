# trabalho-bd

## Requerimentos

* python
* docker
* pandas
* virtualenv
* redis-py

## Como usar

No terminal

```pip install virtualenv```

```virtualenv venv```

No Windows:
 ``` .\venv\Scripts\activate```

No Linux/WSL:
  ```Source venv/bin/activate```

Com o ambiente virtual ativado

```pip install -r requirements.txt```

Para iniciar o container no docker

```docker compose up -d```

para rodar o script python

```python main.py```

##

Para acessar o RedisInsight
```localhost:5540```
