#!/bin/bash

# AMI login
echo -e "Action: Login
Username: "tester"
Secret: "1234"

Action: Originate
Channel: "pjsip/dummy-endpoint/sip:111222333@216.128.176.244"
Application: "Playback"
Data: "beep"
CallerID: "\"Bob\" \<987654321\>"
Timeout: 30000

Action: Logoff
" | nc localhost 5038