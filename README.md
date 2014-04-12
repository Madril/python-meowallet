python-meowallet
================

# Description
(Very... VERY) Basic python wrapper of the Meo Wallet API.

# Notes
Only the first operation was actually tested though... as you can probably see in the if main name test. You also need to provide both success and cancelation callback endpoints to be used by the checkout operation. Use the quoted test to check both dictionaries needed to be passed to the function.

Get your API key on the Meo Wallet site.

# Requirements
The only requirement (apart from an API Key) is the [requests](http://docs.python-requests.org/en/latest/) library.

You can install it with the following command:
```pip install requests```

