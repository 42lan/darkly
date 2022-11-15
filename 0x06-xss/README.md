# Cross Site Scripting (XSS)

[Feedback form](http://192.168.56.101/?page=feedback) has event attribute `onsumbit` that call function to validated it, by JavaScript, so that the value of `Name` and `Message` isn't empty.
  ```js
function validate_required(field,alerttxt)
{
  with (field) {
    if (value==null||value=="") {
      alert(alerttxt);return false;
    }
    else {
      return true;
    }
  }
}

function validate_form(thisform) {
  with (thisform) {
    if (validate_required(txtName,"Name can not be empty.")==false) {
      txtName.focus();return false;
    }
    if (validate_required(mtxMessage,"Message can not be empty.")==false) {
      mtxMessage.focus();return false;
    }
  }
}
```

## Reference Errors
1. `onClick` attribute reference undefined function `checkForm()`.

2. Following code line reference non-existent variable (typo `mtxMessage` that should be `mtxtMessage` as defined in HTML form), it is why the message can be empty.
```js
validate_required(mtxMessage,"Message can not be empty.")
```
![image](https://user-images.githubusercontent.com/22397481/201078471-8ac15945-971f-4652-9071-96a1fd78dbd0.png)


However, it do not check if the user input contains HTML tags or JS script.

> The limitation can be bypassed by removing [`maxlength` attribute](https://www.w3schools.com/tags/att_input_maxlength.asp) on `txtName` and `mtxtMessage` input fields.

## Remediation
[Validate user input](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) to prevent save malformed data.
