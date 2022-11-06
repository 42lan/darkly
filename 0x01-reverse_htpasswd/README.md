# Reverse hashed password

Considering `htpasswd` that has been found at [[WSTG-INFO-03] Web server metafiles & information leakage](https://github.com/42lan/darkly/blob/main/0x00-information_gathering.md#wstg-info-03-web-server-metafiles--information-leakage), lets analyse it.

[`htpasswd`](https://en.wikipedia.org/wiki/.htpasswd) is a canonical name used to store username and hashed password for basic authentification on HTTP server. Optionally, password is prepended by an algorithm specifier.

As there is not specified, a [quick search](https://md5.gromweb.com/?md5=437394baff5aa33daa618be47b75cb49) of hashed password reveal that reverse equals to the following string `qwerty123@`.

Confirm that by calculating md5 message digest on local machine.
```sh
┌──$ [~/42/2022/darkly]
└─>  echo -n "qwerty123@" | md5
437394baff5aa33daa618be47b75cb49
```

By loging with username `root` and password `qwerty123@` on http://192.168.56.101/admin, gives the flag.

## Remediation
- `htpasswd` should not be accessible/fetchable within web server space with a browser
- Enable password complexity requirements
- Use a salt to make dictionary attack more difficult
