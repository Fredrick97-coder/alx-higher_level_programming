#!/usr/bin/python3

def lookup(obj):
    """
    Return the list of available attributes
    and methods of an object.
    """
    return [attr for attr in dir(obj)]
