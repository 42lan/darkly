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
<details>
<summary>cURL htpasswd</summary>

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
</details>

## [WSTG-INFO-04] Web server applications

### Using automated scanning tools
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

Scanning tools show that only one HTTP service on default port 80 is running on the server.

## [WSTG-INFO-05] Webpage content & information leakage
[One webpage](http://192.168.56.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f) contains comments.
<details>
<summary>Webpage comments with useful/useless comments</summary>

```sh
┌──$ [~/42/2022/darkly]
└─>  curl -s "http://192.168.56.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" | tr '\n' ' ' | grep -o '<!-- .* -->'
<!-- Header -->                 <header id="header" >                                                           <a href=http://192.168.56.101><img src=http://192.168.56.101/images/42.jpeg height=82px width=82px/></a>                                                                 <nav id="nav">                                  <ul>                                    <li><a href="index.php">Home</a></li>                                            <li><a href="?page=survey">Survey</a></li>                                              <li><a href="?page=member">Members</a></li>                                      </ul>                           </nav>                  </header>               <!-- Main -->                   <section id="main" class="wrapper">                              <div class="container" style="margin-top:75px"> <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay"> </audio> <script language="javascript">function coucou(){document.getElementById('best_music_ever').play();}</script>  Les Diomédéidés (Diomedeidae) sont une famille d'oiseaux de mer, de l'ordre des Procellariiformes, dont le nom usuel est spécifiquement albatros en français. Ces volatiles sont connus pour détenir le record de la plus grande envergure de toutes les espèces d'oiseaux actuels, celle des grands albatros du genre Diomedea pouvant atteindre 3,4 m, rendant la phase d'envol difficile. Ils planent en revanche sans effort grâce à ces grandes ailes, en utilisant les vents pour les porter sur de grandes distances, comme le font à leur image les avions planeurs. <p style="font-size:0.8em; font-style:italic; color:#666; text-transform: none;"><a href="https://fr.wikipedia.org/wiki/Albatros">Source: Wikipedia</a></p> <br /> <center><a href="https://www.youtube.com/watch?v=Bznxx12Ptl0"><img src="images/albatroz.jpg" onload="coucou()"/></a></center>                                                                                                                                                                                                                                                                                                                                                                  <!-- Voila un peu de lecture :  Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.   -->    <!--   Fun right ? source: loem. Good bye  !!!!  -->                                                                                                         <!-- You must come from : "https://www.nsa.gov/". -->                                                                                                              <!-- Where does it come from? Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.  The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.   -->                                                                                                <!--                                                Let's use this browser : "ft_bornToSec". It will help you a lot.                       -->                               </div>                  </section>              <!-- Footer -->
```
</details>
