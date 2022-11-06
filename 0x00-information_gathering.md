# Information Gathering

## [WSTG-INFO-02] Web server fingerprintint - [Banner grabbing](https://en.wikipedia.org/wiki/Banner_grabbing)

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
```
</details>
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
The `X-Powered-By` field specifies the technology used by the web server which is [PHP 5.5.9-1](https://prototype.php.net/versions/5.5.9/).
That information will narrow down a list of applicable exploits.

## Using automated scanning tools
Automated scanning tools are used within [Dynamic application security testing (DAST)](https://owasp.org/www-community/Vulnerability_Scanning_Tools) and are able to perform more robust scans.
<details>
<summary>Using Nmap</summary>

```sh
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sV -O -A 192.168.56.101
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-06 06:29 EST
Nmap scan report for 192.168.56.101
Host is up (0.0016s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.4.6 (Ubuntu)
| http-robots.txt: 2 disallowed entries
|_/whatever /.hidden
|_http-title: BornToSec - Web Section
|_http-server-header: nginx/1.4.6 (Ubuntu)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=11/6%OT=80%CT=1%CU=33514%PV=Y%DS=2%DC=T%G=Y%TM=63679AB
OS:A%P=x86_64-pc-linux-gnu)SEQ(SP=11%GCD=FA00%ISR=9C%TI=I%CI=RD%TS=U)OPS(O1
OS:=M5B4%O2=M5B4%O3=M5B4%O4=M5B4%O5=M5B4%O6=M5B4)WIN(W1=FFFF%W2=FFFF%W3=FFF
OS:F%W4=FFFF%W5=FFFF%W6=FFFF)ECN(R=Y%DF=N%T=41%W=FFFF%O=M5B4%CC=N%Q=)T1(R=Y
OS:%DF=N%T=41%S=O%A=S+%F=AS%RD=0%Q=)T2(R=Y%DF=N%T=100%W=0%S=Z%A=S%F=AR%O=%R
OS:D=0%Q=)T3(R=Y%DF=N%T=100%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T4(R=Y%DF=N%T=100%
OS:W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=N%T=100%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q
OS:=)T6(R=Y%DF=N%T=100%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=N%T=100%W=0%S=Z
OS:%A=S%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=3D%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%
OS:RUCK=G%RUD=G)IE(R=N)

Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT     ADDRESS
1   0.79 ms 10.0.2.2
2   0.84 ms 192.168.56.101

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.97 seconds
```
</details>
<details>
<summary>Using Nikno</summary>

```sh
┌──(kali㉿kali)-[~]
└─$ nikto -host http://192.168.56.101
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LC_CTYPE = "UTF-8",
        LC_TERMINAL = "iTerm2",
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to a fallback locale ("en_US.UTF-8").
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.56.101
+ Target Hostname:    192.168.56.101
+ Target Port:        80
+ Start Time:         2022-11-06 06:25:54 (GMT-5)
---------------------------------------------------------------------------
+ Server: nginx/1.4.6 (Ubuntu)
+ Retrieved x-powered-by header: PHP/5.5.9-1ubuntu4.29
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Cookie I_am_admin created without the httponly flag
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OSVDB-3268: /whatever/: Directory indexing found.
+ Entry '/whatever/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Entry '/.hidden' in robots.txt returned a non-forbidden or redirect HTTP code (301)
+ "robots.txt" contains 2 entries which should be manually viewed.
+ nginx/1.4.6 appears to be outdated (current is at least 1.14.0)
+ OSVDB-3092: /admin/: This might be interesting...
+ OSVDB-3092: /css/: This might be interesting...
+ OSVDB-3092: /includes/: This might be interesting...
+ OSVDB-3093: /admin/index.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ 7931 requests: 7 error(s) and 14 item(s) reported on remote host
+ End Time:           2022-11-06 06:26:16 (GMT-5) (22 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```
</details>

## Remediation
Exposing server information can lead attacker to find version-specific vulnerabilities that can be used.

It is recommended to :
- Obscure web server information in headers
- Use proxy server to leave client with no knowledge of the web server behind

## [WSTG-INFO-03] Web server metafiles & information leakage
In previous section, Automated Scanning Tools showed that [`robots.txt`](https://www.robotstxt.org/robotstxt.html) lies on the server that contains instructions about the server.
```sh
┌──$ [~/42/2022/darkly]
└─>  curl http://192.168.56.101/robots.txt
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```
It reveals that `/whatever` and `/.hidden` directories are present on the server.

[`/whatever`](http://192.168.56.101/whatever) contains a file name [`htpasswd`](http://192.168.56.101/whatever/htpasswd).
```sh
┌──$ [~/42/2022/darkly]
└─>  curl http://192.168.56.101/whatever/
<html>
<head><title>Index of /whatever/</title></head>
<body bgcolor="white">
<h1>Index of /whatever/</h1><hr><pre><a href="../">../</a>
<a href="htpasswd">htpasswd</a>                                           29-Jun-2021 18:09                  38
</pre><hr></body>
</html>
┌──$ [~/42/2022/darkly]
└─>  curl -LO http://192.168.56.101/whatever/htpasswd
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    38  100    38    0     0   5727      0 --:--:-- --:--:-- --:--:--  6333
┌──$ [~/42/2022/darkly]
└─>  file htpasswd
htpasswd: ASCII text
┌──$ [~/42/2022/darkly]
└─>  cat htpasswd
root:437394baff5aa33daa618be47b75cb49
```
