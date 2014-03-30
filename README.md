# PyQt Web Wrapper

This framework serves as a simple way to embed web applications into a single application.


## Usage

1. Edit ``./config.json`` such that it points to your index.html
2. Your index.html has to include the following files in the same order:
    * ``./view/libs/EventEmitter/EventEmitter.js``
    * ``./view/libs/jquery-2.1.0.min.js``
    * ``./view/js/events.js``
    * ``./view/js/core.js``
3. Check the documentation for a list of provided methods


## Documentation

An object called``PyInterface`` which allows access to more sophisticated functions is provided in javascript.
These functions are listed here.

### log(str)
#### Description
Easy logging to cmd-line using javascript.
#### Example
    PyInterface.log("Everything is fine so far...");
    
### more to come