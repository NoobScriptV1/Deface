#!/usr/bin/python
# — encoding: utf-8 —

import os,sys,time

os.system('clear')

print "Author : B0C1L Gans"
print "Team : Light Cyber Indonesia"
print "WhatsApp : +62 856-9215-8837"
print "Fungsi : Membuat Script Deface Dengan Mudah!"
print ""
print ""
print ""
title = raw_input("<!> Title/Judul >> ")
logo = raw_input("<!> Link logo/Foto >> ")
musik = raw_input("<!> Link musik >> ")
hek = raw_input("<!> Hacked By >> ")
tim = raw_input("<!> Team lu >> ")
kata = raw_input("<!> Kata Kata Lu >> ")

#open index
fo = open("NoobV1.html","w")

nub1 = """<!-- Coded By. . B0C1L Gans -->
<html>
    <head>
        <title>"""
nub2 = title
nub3 = """</title>
<meta property="og:description" content="-=: Created by. NoobScriptV1 :=-">
<link rel="icon" href='"""
nub4 = logo
nub5 = """' type="image/x-icon"/>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Kelly+Slab" type="text/css"/>
<style
type="text/css">body { background-image:
background-color:black; }</style>
<style type="text/css">
html {
	background:#000000;
	font-family: "Kelly Slab";
} 
jack {
	color:#000000;
	-webkit-text-stroke: 0.05em #ffffff;
} 
input,select,textarea{
    border: 1px #ffffff solid;
    -moz-border-radius: 5px;
    -webkit-border-radius:5px;
    border-radius:5px;
    
</style>
</head>
<body>
 <div style="position: fixed; top: 75px; left: -225px; width: 600px; padding: 10px; font-size: 24px; text-align: center; color: white; font-family: 'trebuchet ms', verdana, arial, sans-serif;transform: rotate(-45deg);transform-origin: 50% 0px;-o-transform: rotate(-45deg); -o-transform-origin: 50% 0px;-moz-transform: rotate(-45deg); -moz-transform-origin: 50% 0px; -webkit-transform: rotate(-45deg); -webkit-transform-origin: 50% 0px; background-color: Transparent; border: 1px solid rgb(170, 170, 170); z-index: 9999; opacity: 0.5;"><a href="http://www.xnxx.com" style="text-decoration:none;color:white;">YOU NOOB!</a></div>
<style type="text/css">.blink_me{font-size:60px;-webkit-animation-name:blinker;-webkit-animation-duration:2s;-webkit-animation-timing-function:linear;-webkit-animation-iteration-count:infinite;-moz-animation-name:blinker;-moz-animation-duration:2s;-moz-animation-timing-function:linear;-moz-animation-iteration-count:infinite;animation-name:blinker;animation-duration:1s;animation-timing-function:linear;animation-iteration-count:infinite;}@-moz-keyframes blinker{0% {opacity:1.0;}50% {opacity:0.0;}100% {opacity:1.0;}}@-webkit-keyframes blinker{ 0% {opacity:1.0;}50% {opacity:0.0;}100% {opacity:1.0;}}@keyframes blinker{0% {opacity:1.0;}50% {opacity:0.0;}100% {opacity:1.0;}}</style>
<center>
<iframe width="0" height="0" scrolling="no" frameborder="no" allow="autoplay" src='"""
nub6 = musik
nub7 = """' ></iframe>
<img src='"""
nub8 = logo
nub9 = """' height="750px" width="750px"><br>
<br><center><span class="blink_me"><jack><font size="6">Hacked By """
nub10 = hek
nub11 = """</font></jack></span></center><a href="https://lightcyberindonesia.blogspot.com"><h1><center><jack><font size="8"><u>-=: """
nub12 = tim
nub13 = """ :=-</u></jack></h1></a></span>
<center>
<br>
<br>
<font face="Kelly Slab" color="white" size="15px"><marquee scrollamount="95"> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< </marquee></font>
<p align="center">
    <jack>
<font face="Kelly Slab" size="7" >"""
nub14 = kata
nub15 = """</font></jack><br></p>
</span>
<font face="Kelly Slab" color="white" size="15px"><marquee scrollamount="95" direction="right"> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> </marquee></font>
<br><center><jack><font size="3"> - Copyleft 2k19 - </font></jack></center><span class="blink_me"><jack><font size="5">./B0C1L Gans</jack></font></span>
<script src="https://cdn.rawgit.com/bungfrangki/efeksalju/2a7805c7/efek-salju.js" type="text/javascript"> </script> 
</body>
</head>
</html>"""

fo.write(nub1)
fo.write(nub2)
fo.write(nub3)
fo.write(nub4)
fo.write(nub5)
fo.write(nub6)
fo.write(nub7)
fo.write(nub8)
fo.write(nub9)
fo.write(nub10)
fo.write(nub11)
fo.write(nub12)
fo.write(nub13)
fo.write(nub14)
fo.write(nub15)

print "<!>"
print "[+] Script Deface Sukses Dibuat!"
print "[+] Silahkan Pindahkan File Nya"
print "[+] Dengan Menuliskan"
print "[+] mv NoobV1.html /sdcard"


fo.close()



