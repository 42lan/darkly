# Explore the ISO file

All flags as well as breached may be found be exploring the ISO file.
1. Mount the image
```sh
┌──(kali㉿kali)-[~/42/darkly]
└─$ sudo mkdir /mnt/darkly
┌──(kali㉿kali)-[~/42/darkly]
└─$ sudo mount -o loop Darkly_i386.iso /mnt/darkly
```
2. Unsquash `filesystem.squashfs`
```sh
┌──(kali㉿kali)-[~/42/darkly]
└─$ sudo cp /mnt/darkly/casper/filesystem.squashfs ~/42/darkly
┌──(kali㉿kali)-[~/42/darkly]
└─$ sudo unsquashfs filesystem.squashfs
```
3. Search for 64 bytes alphanumerical strings within `/var/www/html` folder
```sh
┌──(kali㉿kali)-[~/42/darkly/squashfs-root]
└─$ grep -roE "[[:alnum:]]{64}" var/www/ 2>/dev/null
var/www/html/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README:d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
var/www/html/index.php:df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
var/www/html/admin/index.php:d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
var/www/html/includes/b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f.inc.php:f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
var/www/html/includes/survey.inc.php:03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa
var/www/html/includes/recover.inc.php:1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0
var/www/html/includes/feedback.inc.php:0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e
var/www/html/includes/redirect.inc.php:b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3
var/www/html/includes/header.inc.php:b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0
var/www/html/includes/footer.inc.php:b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
var/www/html/includes/media.inc.php:928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d
var/www/html/includes/upload.inc.php:46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
var/www/html/includes/upload.inc.php:46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
var/www/html/includes/signin.inc.php:b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2
```
