# wizardryapi
This is just a repo to practice using fastapi.  

To run locally, run the main.py file _python3 main.py_  
Then run the following command: _uvicorn main:app --reload_  
You can then navigate to _http://127.0.0.1:8000/items/_ to view the whole list of available items  

You can also test via API request to the following endpoints:  
/items/{ITEM_NAME}  
This will get you all the information for that particular item

/items/{ITEM_NAME}/price  
This will get you only the price json for the particular item
