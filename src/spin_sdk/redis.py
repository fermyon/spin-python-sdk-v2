"""Module for interacting with a Redis database"""

from spin_sdk.wit.imports.redis import Connection 

def open(connection_string: str) -> Connection:
    """
    Open a connection with a Redis database.
    
    The connection_string is the Redis URL to connect to.

    A `spin_sdk.wit.types.Err(spin_sdk.wit.imports.redis(ErrorInvalidAddress)` will be raised if the connection string is invalid.

    A `spin_sdk.wit.types.Err(spin_sdk.wit.imports.redis(ErrorTooManyConnection)` will be raised if there are too many open connection. Closing one or more Previously opened connection using the `drop` method might help.
    
    A `spin_sdk.wit.types.Err(spin_sdk.wit.imports.redis(ErrorOther(str))` when some other error occurs.
    """
    return Connection.open(connection_string)