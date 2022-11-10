# Path traversal

By requesting [unexesting page](http://192.168.56.101/?page=notexist) an alert pop ups.
![image](https://user-images.githubusercontent.com/22397481/201100502-21b562af-9527-4715-b6d6-436b0c7d85f5.png)

Path traversal attacks aims to access files/directories that are stored outside the web root folder.

Proceeding path traversal, different messages are pop ups, until 7th level with following message: `You can do You can DO it !!!  :]`.


Trying to access \*NIX password file at http://192.168.56.101/?page=../../../../../../../etc/passwd, gives the flag.
