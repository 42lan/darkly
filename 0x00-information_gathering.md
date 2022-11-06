# Information Gathering

## Web server fingerprintint - [Banner grabbing](https://en.wikipedia.org/wiki/Banner_grabbing)

Establish a connection to the web server and send an HTTP request to gain information about the running service on the host, by examining its response header.

<details>
<summary>Using netcat</summary>

```sh
┌──$ [~/42/2022/darkly]
└─>  nc 192.168.56.101 80
HEAD / HTTP/1.0

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Sun, 06 Nov 2022 10:06:35 GMT
Content-Type: text/html
Connection: close
X-Powered-By: PHP/5.5.9-1ubuntu4.29
Set-Cookie: I_am_admin=68934a3e9455fa72420237eb05902327; expires=Sun, 06-Nov-2022 11:06:35 GMT; Max-Age=3600
```
</details>
<details>
<summary>Using telnet</summary>

```sh
┌──$ [~/42/2022/darkly]
└─>  telnet 192.168.56.101 80
Trying 192.168.56.101...
Connected to 192.168.56.101.
Escape character is '^]'.
HEAD / HTTP/1.0

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Sun, 06 Nov 2022 10:08:34 GMT
Content-Type: text/html
Connection: close
X-Powered-By: PHP/5.5.9-1ubuntu4.29
Set-Cookie: I_am_admin=68934a3e9455fa72420237eb05902327; expires=Sun, 06-Nov-2022 11:08:34 GMT; Max-Age=3600

Connection closed by foreign host.
</details>
```
<details>
<summary>Using curl</summary>

```sh
┌──$ [~/42/2022/darkly]
└─>  curl -I 192.168.56.101
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Sun, 06 Nov 2022 10:36:47 GMT
Content-Type: text/html
Connection: keep-alive
X-Powered-By: PHP/5.5.9-1ubuntu4.29
Set-Cookie: I_am_admin=68934a3e9455fa72420237eb05902327; expires=Sun, 06-Nov-2022 11:36:47 GMT; Max-Age=3600
```
</details>

Server is running [Nginx 1.4.6](https://nginx.org/en/CHANGES-1.4) on Ubuntu.
That information will narrow down a list of applicable exploits.
