import os
import os.path
import re

def getCommand1(config):
	playerurl="http://radiko.jp/player/swf/player_3.0.0.01.swf"
	playerfile="/tmp/radiko_player.swf"
	keyfile="/tmp/radiko_authkey.png"

	if not os.path.exists(playerfile):
		command = "wget -q -O %s %s" % (playerfile, playerurl)
		r = config.R(command)
		
		if r is not 0:
			config.P("ERROR failed to get player")
			exit(1)
			
	if not os.path.exists(keyfile):
		command = "swfextract -b 14 %s -o %s" % (playerfile, keyfile)
		r = config.R(command)	
		
		if r is not 0:
			config.P("ERROR failed to get key")
			exit(1)
			
	if os.path.exists("auth1_fms"):			
		os.system("rm auth1_fms")
	
	command = """\
			wget -q \
			--header="pragma: no-cache" \
			--header="X-Radiko-App: pc_1" \
			--header="X-Radiko-App-Version: 2.0.1" \
			--header="X-Radiko-User: test-stream" \
			--header="X-Radiko-Device: pc" \
			--post-data='\r\n' \
			--no-check-certificate \
			--save-headers \
			https://radiko.jp/v2/api/auth1_fms
			"""
	r = config.R(command)			

	if (r is not 0) or not os.path.exists("auth1_fms"):
		config.P("ERROR auth2 failure")
		exit(1)
		
	config.P("auth1 OK")			

	f = open("auth1_fms")
	text = f.read()
	config.P(text)
	f.close()	

	p1 = re.compile(r"x-radiko-authtoken: (.*)", re.I)
	m1 = p1.search(text)
	if not m1:
		config.P("ERROR authtoken not parsed")
		exit(1)
	authtoken = m1.group(1)
	config.P("authtoken: %s" % authtoken)

	p2 = re.compile(r"x-radiko-keyoffset: (.*)", re.I)
	m2 = p2.search(text)
	if not m2:
		config.P("ERROR keyoffset not parsed")
		exit(1)
	keyoffset = int(m2.group(1))
	config.P("keyoffset: %d" % keyoffset)

	p3 = re.compile(r"x-radiko-keylength: (.*)", re.I)
	m3 = p3.search(text)
	if not m3:
		config.P("ERROR keylength not parsed")
		exit(1)
	keylength = int(m3.group(1))		
	config.P("keylength: %d" % keylength)
		
	return None
