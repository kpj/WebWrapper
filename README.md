# PyQt Web Wrapper

This framework serves as a simple way to embed web applications into a single, local application.

## Installation

Install the needed [PyQtX](https://github.com/kpj/PyQtX) package using

    pip install PyQtX


## Usage

1. Call ``main.py`` and provide your main html file as an argument ([example](https://github.com/kpj/WebWrapper/blob/master/start))
2. Your index.html has to include the following file
    * ``./view/include.js``
3. Call ``initWrapper`` and provide additional sources as well as a callback to be executed when all sources are loaded
4. Check the documentation for a list of provided methods


## Documentation

The latest documentation can be generated using doxygen.

Particularly important is the object called ``PyInterface`` which allows access to more sophisticated functions is provided in javascript.
These functions are defined in ``./python/js_interface.py``.
