cookiecutter-fleskful
=====================

A Flask-restful template for cookiecutter_, based on Steven Loria's cookiecutter-flask_ template.

.. _cookiecutter-flask: https://github.com/sloria/cookiecutter-flask
.. _cookiecutter: https://github.com/audreyr/cookiecutter

.. image:: https://travis-ci.org/camphor/cookiecutter-fleskful.svg
    :target: https://travis-ci.org/camphor/cookiecutter-fleskful
    :alt: Build Status

Installation
------------
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/kamforka/cookiecutter-fleskful.git

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.

Features
--------

- Flask-SQLAlchemy as an ORM with basic User model
- Flask-Migrate for easy database migrations
- Flask-Bcrypt for password hashing
- Flask-JWT for token based authentication
- Flask-CORS for cross origin resource sharing
- Flask's Click CLI configured with simple commands
- Flask-Cache for caching
- pytest and Factory-Boy for testing (example tests included)

Inspiration
-----------
- `The cookiecutter-flask project <https://github.com/sloria/cookiecutter-flask/>`_ 
- `Flask-JWT <https://pythonhosted.org/Flask-JWT/>`_
- `RESTful Authentication with Flask <https://blog.miguelgrinberg.com/post/restful-authentication-with-flask/>`_
- `Flask Official Documentation <http://flask.pocoo.org/docs/>`_


License
-------

BSD licensed.

Changelog
---------
0.1.0 (31/05/2017)
******************
- Initial project base
- Tested API endpoints with basic User model
- JWT authentication
- CORS support



