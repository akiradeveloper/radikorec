import os
import os.path
import re
import commands

import xml.etree.ElementTree as ET

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
		config.R("rm auth1_fms")
	
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
		config.P("ERROR auth1 failed")
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
	authtoken = m1.group(1).strip()
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
	
	command = """ \
dd \
if=%s \
bs=1 \
skip=%d \
count=%d \
2> /dev/null | base64
""".strip() % (keyfile, keyoffset, keylength)
	config.P(command)		
	partialkey = commands.getoutput(command)
	config.P("partialkey: %s" % (partialkey))

	config.R("rm auth1_fms")

	if os.path.exists("auth2_fms"):
		config.R("rm auth2_fms")
		
	command = """ \
wget -q \
--header="pragma: no-cache" \
--header="X-Radiko-App: pc_1" \
--header="X-Radiko-App-Version: 2.0.1" \
--header="X-Radiko-User: test-stream" \
--header="X-Radiko-Device: pc" \
--header="X-Radiko-Authtoken: %s" \
--header="X-Radiko-Partialkey: %s" \
--post-data='\r\n' \
--no-check-certificate \
https://radiko.jp/v2/api/auth2_fms
""".strip() % (authtoken, partialkey)
	r = config.R(command)

	if (r is not 0) or not os.path.exists("auth2_fms"):
		config.P("ERROR auth2 failed")
		exit(1)
			
	config.P("auth2 OK")		

	f = open("auth2_fms")
	text = f.read()
	config.P(text)
	f.close()

	areaid = text.split(",")[0].strip()
	config.P("areaid: %s" % areaid)

	config.R("rm auth2_fms")

	channel = config.args.channel
	xmlFile = "%s.xml" % channel
	if os.path.exists(xmlFile):
		config.R("rm %s" % xmlFile)
		
	command = """ \
wget \
-q "http://radiko.jp/v2/station/stream/%s"
""".strip() % xmlFile
	config.R(command)	

	f = open(xmlFile)		
	text = f.read()
	config.P(text)
	f.close()

	root = ET.fromstring(text)
	stream_url = root[0].text
	config.P("stream_url: %s" % stream_url)

	pat = re.compile(r"^(.+)://(.+?)/(.*)/(.*?)$")
	mat = pat.search(stream_url)
	A = mat.group(1)
	B = mat.group(2)
	C = mat.group(3)
	D = mat.group(4)	
	config.P("A: %s, B:%s, C:%s, D:%s" % (A, B, C, D))
	
	config.R("rm %s" % xmlFile)

	command = """ \
%s \
--rtmp %s \
--app %s \
--playpath %s \
-W %s \
-C S:"" -C S:"" -C S:"" -C S:%s \
--live \
-o %s \
--stop %d \
""".strip() % (
		config.args.rtmpbin,
		"%s://%s" % (A, B), C, D,
		playerurl, authtoken, config.filename, config.duration_sec)

	return command
