"""
Example Skill: Greet User

Purpose:
    Demonstrates a simple skill with docstring and usage example.

Parameters:
    name (str): The name of the user to greet.

Returns:
    str: Greeting message.

Example usage:
    >>> greet_user('Alice')
    'Hello, Alice! Welcome to Agent Zero.'
"""

def greet_user(name):
    """Return a greeting message for the user."""
    return f"Hello, {name}! Welcome to Agent Zero."
