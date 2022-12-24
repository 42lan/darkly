# [WSTG-IDNT-01] Forged cookie

Visiting [home page](http://192.168.56.101/) server sends a cookies to be set via Response Headers.

```
Set-Cookie
I_am_admin=68934a3e9455fa72420237eb05902327; expires=Mon, 07-Nov-2022 16:25:44 GMT; Max-Age=3600
```

[A quick search](https://md5hashing.net/hash/md5/68934a3e9455fa72420237eb05902327) shows that reverse of MD5 hash digest equals to the string `false`.

MD5 hash digest of the string `true`
```shell
┌──$ [~/42/2022/darkly]
└─>  echo -n "true" | md5
b326b5062b2f0e69046810717534cb09
```

Changing value of saved cookie and refreshing the page gives the flag.

## Remediation
- Use encrypted value in the cookie
- Verify cookie on server-side
