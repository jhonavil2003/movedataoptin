import azure.functions as func
import logging
import requests

app = func.FunctionApp()

@app.queue_trigger(arg_name="azqueue", queue_name="dataavianca",
                               connection="AzureWebJobsStorage") 
def queue_trigger(azqueue: func.QueueMessage):
    message = azqueue.get_body().decode('utf-8');

    if message:
        logging.info(f"Processing message: {message}") 
