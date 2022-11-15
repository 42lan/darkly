# Unrestricted File Upload

On Upload(http://localhost:4242/?page=upload) page located on the bottom of the main page, there are \<form\> tag with attribute `enctype="multipart/formdata` which enables to locate the location of the file.

Once you click `Browse` button, you will be able to locate the file wish to upload, but only with extension `jpeg` is allowed. 
<img width="1038" alt="image" src="https://user-images.githubusercontent.com/46742040/202015491-9553f16f-c6dc-4b2c-b6d9-c1a84ce4856e.png">
(A screenshot where image is uploaded with no `jpeg` extension)


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

