# Request payload

[Recover password](http://192.168.56.101/?page=recover) page do not provide an field to fill in order to recover the password.

However, looking at the POST request, default value of mail in the body of the request is set to:
```
mail: webmaster@borntosec.com
```

By modifying the value of the mail field in the request payload and submiting a new POST request, give the flag.
