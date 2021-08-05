# rabbitmq_python_client
Python rabbitmq client useful for getting the information required. Will be available as python package soon

## Installation
```
pip install git+https://github.com/kaskou/rabbitmq_python_client
```

## Overview
* Package import
  
    ```buildoutcfg 
        from rabbitmq_api_client import rabbitmq_api_client
    ```
  
* All the API(HTTP) operations need to be initiated by
    ```buildoutcfg
        client=rabbitmq_api_client.rabbit_conn(url, user, password)
    ```
###Queue Operations
```buildoutcfg
    # Get the List of Queues
    client.ListQueues()
```

Inspiration from this Go Github Repo `https://github.com/michaelklishin/rabbit-hole`