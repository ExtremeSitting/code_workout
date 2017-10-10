#### Resources:
apt packages:
* python2.7
* python-pip

pip packages:
* virtualenv
* virtualenvwrapper
* requests
* flask

#### Files:
thing-app.py

sysinfo.py

#### Process:
Review the thing_app.py script. It is a very small and simple api. It supports `GET`, `POST`, and `DELETE` requests. The *name* key is the only required key when making a `POST`.

Example `POST` data:
```json
{
    "name": "system_load", 
    "value": 1, 
    "device": "phillip"
}
```

* `GET` requests to `http://localhost:5000/things` will return all things posted.
* `GET` requests to `http://localhost:5000/things/<id>` will return the thing assigned to that id.
* `POST` requests to `http://localhost:5000/things` will load the provided data in the app and will return the full record generated.
* `DELETE` requests to `http://localhost:5000/things/<id>` will delete the thing from the list of things.

|Verb|URI|Action|
--- | --- | --- |
GET|`http://localhost:5000/things`|Return all things
GET|`http://localhost:5000/things/<id>`|Return the thing with that ID
POST|`http://localhost:5000/things`|Load and return the record
DELETE|`http://localhost:5000/things/<id>`|Delete the thing with that ID

**The key requirements for `POST` commands are intentionally minamal.**

#### Prep:
Run:

```pip install virtualenv virtualenvwrapper
mkvirtualenv code_workout
workon code_workout
pip install flask requests
python thing_app.py
```
Then in another console:

`python sysinfo.py` to preload things.

The `thing_app.py` script will need to stay running in a console while you interact with it in another console.

#### Goals:
Use a name that is descriptive of the value you provide in all posted data.
1. `GET` The current list of things posted.
2. `POST` system load, free ram, and current used disk space for / with a new device name.
3. Iterate through the list of all things and issue a `DELETE` to any record that doesn't match your device's exact hostname.
4. `GET` all the things and form the json output into CSV (Comma Seperated Values) with the device's name as the first value.

#### For the bold:
 Write a script that sends the system load to the thing api every 10 seconds. Write another script that reads from the api that posts free memory and the current date and time as an additional key and value when the 1 minute average excedes 15 minute average by at least 10%.

#### Notes:
You'll need to be in the 'code_workout' virtualenv if you want to run the app or the sysinfo script, but you wont have to install the requirements again.

**Make sure to use your 'answers' branch locally for all your work.**
