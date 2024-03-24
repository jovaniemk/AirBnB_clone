#AirBnB_clone
In this project we work on differnt classes which will be later used
to characterize the user which will use the AirBnB website, places,  city
state and other things. we also define our FileStorage class which will save
the previously created objects into some file as JSON representation, and also
retrive the object representation from the json file.
we write console.py which we will use to :-
        -> Create a new object (ex: a new User or a new Place)
        -> Retrieve an object from a file, a database etc…
        -> Do operations on objects (count, compute stats, etc…)
        -> Update attributes of an object
        -> Destroy an object
to start a command interpreter we will use eithe python3 console.py or ./console.py in shell
and then we will type commands that are defined in console.py file to do differnt tasks.

example >> represents the shell
>> ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) create BaseModel
78e896dd-eff1-47c5-b423-33f6fc58c708
(hbnb) all
["[BaseModel] (40dd4995-5126-4c2c-97e1-86213168c785) {'id': '40dd4995-5126-4c2c-97e1-86213168c785', 'created_at': datetime.datetime(2024, 3, 23, 3, 56, 27, 505995), 'updated_at': datetime.datetime(2024, 3, 23, 3, 56, 27, 506057), 'name': 'My First Model', 'my_number': 89}", 
"[BaseModel] (78e896dd-eff1-47c5-b423-33f6fc58c708) {'id': '78e896dd-eff1-47c5-b423-33f6fc58c708', 'created_at': datetime.datetime(2024, 3, 24, 3, 51, 44, 752221), 'updated_at': datetime.datetime(2024, 3, 24, 3, 51, 44, 752221)}"]
(hbnb) quit
>>
