Requirements
===========

* Python 2.7
* Works on Linux, Windows, Mac OSX and (quite possibly) BSD.

Install
=======

The quick way is use the provided `make` file.

<code>
$ make install
</code>

Starting and Stopping Services
==============================

To launch the services:

<code>
$ make launch
</code>

To stop the services: 

<code>
$ make shutdown
</code>


APIs and Documentation
======================

## Movie Service (port 5005)

This service is used to get a list of nth fibonaci numbers.
To lookup all movies in the database, hit: `http://127.0.0.1:5005/fib/<nth>`


    GET /movies

    RETURNS a list of n fibonaci numbers, in this case : http://127.0.0.1:5005/fib/9
    
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
