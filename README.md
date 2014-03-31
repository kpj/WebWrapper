# PyQt Web Wrapper

This framework serves as a simple way to embed web applications into a single, local application.


## Usage

1. Edit ``./config.json`` such that it points to your index.html
2. Your index.html has to include the following file
    * ``./view/include.js``
3. Call ``initWrapper`` and provide a callback to be executed when all sources are loaded
4. Check the documentation for a list of provided methods


## Documentation

The latest documentation can be generated using doxygen.

Particularly important is the object called ``PyInterface`` which allows access to more sophisticated functions is provided in javascript.
These functions are defined in ``./python/js_interface.py``.
