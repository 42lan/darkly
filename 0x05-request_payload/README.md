# Request payload

[Recover password](http://192.168.56.101/?page=recover) page do not provide an field to fill in order to recover the password.

However, looking at the POST request, default value of mail in the body of the request is set to:
```
mail: webmaster@borntosec.com
```

![image](https://user-images.githubusercontent.com/22397481/201653483-5c57ee82-d737-444e-98b2-6dcc30e69922.png)
![image](https://user-images.githubusercontent.com/22397481/201653255-9c792506-3740-4eb5-b56d-13c7c0584355.png)

By modifying the value of the mail field in the request payload and submiting a new POST request, give the flag.

## Remediation
- Remove hidden input element with webmaster's e-mail
