# Poke-Getter

## To Run

* Clone the repository
* `pip install -r requirements.txt`
* Set the FLASK_APP environment variable 
  * `$ export FLASK_APP=main.py`
* Then run the app
  * `$ flask run`
 * To send a request, hit the `/pokemon/catch/` endpoint, like so:
   * `$ curl -X GET http://127.0.0.1:5000/pokemon/catch?habitat_name=cave&type=flying`