# radikorec
A Simple Radiko/Radiru Recorder

## Example
The command below nicely helps you learn english. Enjoy!

```
radikorec 
--channel NHK2 
--duration 15 
--prefix BUSINESS_ENGLISH 
--directory /home/akira/radio
```

## Install
`make install` or  
`pip install radikorec` (not available right now)

## Test
First, run with `--test` flag to see if it works.  
Starts to record streaming for 5 second and stores it as /tmp/RADIKOREC.m4a
is the right behavior  
otherwise check for /tmp/radikorec.log
which might help you.  
Any question will be welcome. Feel free to e-mail me (Japanese OK).

## Dependencies
* [rtmpdump](https://github.com/svnpenn/rtmpdump) >= 2.4. You may have to build by hand.  
* ffmpeg. 
* [swftools](http://www.swftools.org/download.html). Debian squeeze doesn't have the package. Build by yourself. 

## Author
Akira Hayakawa (@akiradeveloper)  
ruby.wktk@gmail.com
