# Improper Data Validation

[Survey page](http://192.168.56.101/index.php?page=survey) allow to grade a subject from 1 to 10.

However, by changing the value of `&valeur=` in the body of POST request, allow to grade subject with a value greater that 10.

![image](https://user-images.githubusercontent.com/22397481/207578095-d0d68dac-8484-49df-9aeb-28ee9d7bf2a3.png)

... or simply by changing the value of an option in the form
![image](https://user-images.githubusercontent.com/22397481/207579504-b9d71b83-dfdf-4a6c-8efa-3e668f41a63f.png)
