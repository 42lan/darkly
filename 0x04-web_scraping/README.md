# Web scraping
Web scraping is an automatic way to collect content and data form the website.

Using home made Python script, scrap the content of http://192.168.56.101/.hidden/, which will append the content of README files into README file. Then print only unique lines using `sort` command.

```shell
┌──$ [~/42/2022/darkly/0x04-web_scraping]
└─>  ./scraper.py
┌──$ [~/42/2022/darkly/0x04-web_scraping]
└─>  sort -u README
Demande Ã  ton voisin de droite  
Demande Ã  ton voisin de gauche  
Demande Ã  ton voisin du dessous 
Demande Ã  ton voisin du dessus  
Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
Non ce n'est toujours pas bon ...
Toujours pas tu vas craquer non ?
Tu veux de l'aide ? Moi aussi ! 
```
## Remediation
- Detect web scraping in order to block
- State in the terms and conditions a prohibition on web scraping
