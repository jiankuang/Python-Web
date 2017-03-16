# What is CDP
Smart+Connected Digital Platform

# How to connect to CDP using Python script
* Follow the lab instruction: https://learninglabs.cisco.com/modules/cdp/cdp101/step/1
* Clone lab code form: https://github.com/CiscoDevNet/scc-cdp-api-examples
* Open DevNet Sandbox: https://devnetsandbox.cisco.com/RM/Diagram/Index/27451827-d6a8-4aa6-a3f1-0125e8a8a0f7?diagramType=Topology
* Download Cisco AnyConnect, then you will get an email about VPN credential, then connect to VPN
* Ping 10.10.20.6 success, which is the IP of sandbox
* In the same email, you will get cerdential to login to CDP, replace username and password in the code you cloned from Github. 
* This code run on Python3. So download python3, change python.exe to python3.exe, put it into PATH. 
* Run `python3 cdp101_python_example.py`, you will be able to connect to CDP, and get api_access_token and app_access_token. 
