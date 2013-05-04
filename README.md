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
`make install` or  
`pip install radikorec` (not available right now)

There are few programs you may have to build by yourself.  
Assume we install the programs under /usr/local with default prefix.
### rtmpdump
1. `git clone` the program  
2. `$ make SYS=posix`  
3. `# make install`  
4. Don't forget to add /usr/local/lib to LD_LIBRARY_PATH

### swftools
1. Download the archive and inflate it.  
2. Just the ordinary build procedure. `$ ./configure`, `$ make` and `# make install`.

## Test
First, run with `--test` flag to see if it works.  
Starts to record streaming for 5 second and stores it as /tmp/RADIKOREC.m4a
is the right behavior  
otherwise check for /tmp/radikorec.log
which might help you.  
Any question will be welcome. Feel free to e-mail me (Japanese OK).

## Author
Akira Hayakawa (@akiradeveloper)  
ruby.wktk@gmail.com
