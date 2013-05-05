# radikorec
A Simple Radiko/Radiru Recorder

## Example
The command below nicely helps you learn english. Enjoy!
```
radikorec 
--channel=NHK2 
--duration=15 
--prefix=BUSINESS_ENGLISH 
--directory=/home/akira/radio
```
## Dependencies
* [rtmpdump](https://github.com/svnpenn/rtmpdump) >= 2.4  
* [swftools](http://www.swftools.org/download.html)  
* ffmpeg   

## Install
`make install`(recommended) or `pip install radikorec`.

There are few programs you may have to build by yourself.  
run `./compile` and then `./setup`.  

## Test
First, `./runtest` to see if it works.  
Starts to record streaming for 1 minute and stores it in /tmp is the correct behavior.  
Check for /tmp/radikorec.log which might help you.  
Any question will be welcome. Feel free to e-mail me (Japanese OK).

## Author
Akira Hayakawa (@akiradeveloper)  
ruby.wktk@gmail.com
