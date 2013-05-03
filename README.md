# radikorec
A Simple Radiko/Radiru Recorder

## Usage
Simple interface.

> usage: radikorec [-h] [--duration DURATION] [--prefix PREFIX]
>                  [--rtmpbin RTMPBIN] [--channel CHANNEL]
>                  [--directory DIRECTORY] [--test] [--debug] [--dry-run]
> 
> A Simple Radiko Recorder
> 
> optional arguments:
>   -h, --help            show this help message and exit
>   --duration DURATION   time(min) to record. default(1)
>   --prefix PREFIX       filename prefix. default(RADIKOREC)
>   --rtmpbin RTMPBIN     The path for rtmpdump binary >= 2.4. default(rtmpdump)
>   --channel CHANNEL     FM|NHK1|NHK2. default(FM)
>   --directory DIRECTORY
>                         output directory. default(/tmp)
>   --test                set test parameters.
>   --debug               print messages on console.
>   --dry-run             don't actually execute

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
