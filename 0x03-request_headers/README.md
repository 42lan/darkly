# Request headers

The source of [the page](http://192.168.56.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f) contains few comments.

```sh
┌──$ [~/42/2022/darkly]
└─>  curl -s "http://192.168.56.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" | tr '\n' ' ' | grep -o '<!-- .* -->'
<!-- Header -->                 <header id="header" >                                                           <a href=http://192.168.56.101><img src=http://192.168.56.101/images/42.jpeg height=82px width=82px/></a>                                                                 <nav id="nav">                                  <ul>                                    <li><a href="index.php">Home</a></li>                                            <li><a href="?page=survey">Survey</a></li>                                              <li><a href="?page=member">Members</a></li>                                      </ul>                           </nav>                  </header>               <!-- Main -->                   <section id="main" class="wrapper">                              <div class="container" style="margin-top:75px"> <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay"> </audio> <script language="javascript">function coucou(){document.getElementById('best_music_ever').play();}</script>  Les Diomédéidés (Diomedeidae) sont une famille d'oiseaux de mer, de l'ordre des Procellariiformes, dont le nom usuel est spécifiquement albatros en français. Ces volatiles sont connus pour détenir le record de la plus grande envergure de toutes les espèces d'oiseaux actuels, celle des grands albatros du genre Diomedea pouvant atteindre 3,4 m, rendant la phase d'envol difficile. Ils planent en revanche sans effort grâce à ces grandes ailes, en utilisant les vents pour les porter sur de grandes distances, comme le font à leur image les avions planeurs. <p style="font-size:0.8em; font-style:italic; color:#666; text-transform: none;"><a href="https://fr.wikipedia.org/wiki/Albatros">Source: Wikipedia</a></p> <br /> <center><a href="https://www.youtube.com/watch?v=Bznxx12Ptl0"><img src="images/albatroz.jpg" onload="coucou()"/></a></center>                                                                                                                                                                                                                                                                                                                                                                  <!-- Voila un peu de lecture :  Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.   -->    <!--   Fun right ? source: loem. Good bye  !!!!  -->                                                                                                         <!-- You must come from : "https://www.nsa.gov/". -->                                                                                                              <!-- Where does it come from? Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.  The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.   -->                                                                                                <!--                                                Let's use this browser : "ft_bornToSec". It will help you a lot.                       -->                               </div>                  </section>              <!-- Footer -->
```
```html
<!-- You must come from : "https://www.nsa.gov/". -->
<!-- Let's use this browser : "ft_bornToSec". It will help you a lot. -->
```

They are instruction to perfom in order to obtain the flag.

Request headers needs to be set with those quoted values.

1. `Referer` is a HTTP header contains the address from which a resource has been requested.
2. `User-Agent` is a HTTP header that let server identify the application/OS/vendor/version of the requesting user agent (computer program representing a person, for example, a browser in a Web context).

<details>
<summary>Using curl</summary>

```sh
┌──$ [~/42/2022/darkly]
└─>  curl -s -H "Referer: https://www.nsa.gov/" -H "User-Agent: ft_bornToSec" "http://192.168.56.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" | grep flag
<center><h2 style="margin-top:50px;"> The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
```
</details>

<details>
<summary>Using plugin</summary>

Using the plugin [ModHeader](https://modheader.com/) they can be substitued.
```
Referer:https://www.nsa.gov/
User-Agent:ft_bornToSectrash:///request_headers%20referer%20user-agent.png
```
![request_headers referer user-agent](https://user-images.githubusercontent.com/22397481/200792965-25c908e1-2cc5-4cd3-854a-bcdc1dd86f00.png)

</details>
