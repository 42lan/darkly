# [WSTG-CLNT-04] Client-side URL redirect

In the footer of the [website](http://192.168.56.101/) 3 social media links redirect user to 42born2code page.

```
http://192.168.56.101/index.php?page=redirect&site=facebook
http://192.168.56.101/index.php?page=redirect&site=twitter
http://192.168.56.101/index.php?page=redirect&site=instagram
```

By changing valeu of `site` other than 3 social media name, gives the flag.

![image](https://user-images.githubusercontent.com/22397481/201696064-3cf35a61-a59a-4ea8-acb0-72f943b46724.png)
