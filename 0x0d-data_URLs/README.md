# Cross Site Scripting (XSS) - Data URLs

there is an image located with click available. Once click to the image, it will be redirected to this address http://{IP_ADDR}/?page=media&src=nsa, as the \<a\> tag with attribute `href=?page=media&src=nsa` was provided, as the browser shows `404 Not Found` inside the page. By navigating the actual page, the `<table>` tag have `<object>` element, which will be passed from the query string parameter `src`. As stated on [Data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs), the URLs prefixed with the `data:` schems allow to embed small files inline in documents.

So, by editing paramter to query string `src=` to `data:text/html,%3Ch1%3EHello%2C%20World%21%3C%2Fh1%3E` will display 'Hello, World!' to the browser.



# Remedattion
