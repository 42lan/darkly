# Cross Site Scripting (XSS) - Data URLs

there is an image located with click available. Once click to the image, it will be redirected to this address http://{IP_ADDR}/?page=media&src=nsa, as the \<a\> tag with attribute `href=?page=media&src=nsa` was provided, as the browser shows `404 Not Found` inside the page. By navigating the actual page, the `<table>` tag have `<object>` element, which will be passed from the query string parameter `src`. As stated on [Data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs), the URLs prefixed with the `data:` schems allow to embed small files inline in documents.

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
