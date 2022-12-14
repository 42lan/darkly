# Cross Site Scripting (XSS) - Data URLs

In the first section of the home page, an image redirect to [the location](http://192.168.56.101/?page=media&src=nsa) where an `object` tag specifies the URL of NSA logotype, via `data` attribute.

The value of `data` attribute change accordingly the value GET parameter `src` in the URL.

Using special format, called [data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs), in `src` allow to embed small inline data in HTML document.

So, by editing paramter to query string `src=` to `data:text/html,%3Ch1%3EHello%2C%20World%21%3C%2Fh1%3E` will display 'Hello, World!' to the browser.

<img width="442" alt="image" src="https://user-images.githubusercontent.com/46742040/202878504-fda66088-c43e-48e8-bcd3-7092ba648d69.png">
(a browser image showing `Hello, World!`)

Not only any data can be passed, but script can be passed to this tag and this means the code can be executed, as shown on the [example](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs)

<img width="800" alt="image" src="https://user-images.githubusercontent.com/46742040/202879013-06386e15-be43-4894-9a3c-c3630a569a0e.png">
(a browser with script alert('hi'))

By tring base64 encoded string for the `src` paramter, with [appropriate syntax](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs#syntax), the following address will give the flag

```
$ echo -n '<script>alert('hi');</script>' | base64
PHNjcmlwdD5hbGVydChoaSk7PC9zY3JpcHQ+

$ curl http://{IP_ADDR}/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnaGknKTs8L3NjcmlwdD4\=
[...]
The flag is : 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d
[...]
```

# Remedattion
- https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
- https://owasp.org/www-community/attacks/xss/
