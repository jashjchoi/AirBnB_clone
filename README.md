# 0x00. AirBnB clone - The console
In this project we will be creating a parent class to handle initialization, serialization and deserialization of your future instances. as well as a file storage engine to to create a simple flow there of.
we will also be creating all  classes used for Airbnb in addition to all unittest to validate our classes and storage engine
## The Console
the console itself is a command interpreter whis is activated through the command  './console.py' from therw you can enter:
 * help
   * list all availble commands and their explantions: 
   * `quit`, `all`, `show`, `create`, `destroy`, `update` 
 * all
   * list everything(or if specified all of a certain type of object) that is stored in the json file
   * example: `all BaseModel` 
 * show
   * shows a specific instance of an object type
   * example: `show BaseModel 55044e70-f8b1-4b51-85f1-f682c5084792`
 * create
   * creates an instance of a model
   * example: `create BaseModel`
 * destroy
   * destroys a specific instance of a model
   * example: `destroy BaseModel 55044e70-f8b1-4b51-85f1-f682c5084792`
 * update
   * updates attributes in specific model or creates new attributes in specific model
   * example: `update BaseModel 55044e70-f8b1-4b51-85f1-f682c5084792 first-name "Betty"`
