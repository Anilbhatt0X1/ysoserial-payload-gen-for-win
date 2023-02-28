## Description
The payload_generator tool generates payloads for various types of exploits 
It utilizes the open-source tool ysoserial, which can be used to generate serialized Java objects for exploitation. The tool accepts a command and an operating system as input and generates payloads for different exploits, including remote code execution and command injection. 

The generated payload can be used to do intruded testing in Target to detect the vulnerability


# ysoserial-payload-gen-for-win

requirement .

`wget https://github.com/frohoff/ysoserial/releases/download/v0.0.6/ysoserial-all.jar`


How to use it.

```shell
python Gen-ysoserial-win.py -h
usage: Gen-ysoserial-win.py [-h] {Windows,Linux} cmd POC

positional arguments:
  {Windows,Linux}  Name of the operating system
  cmd              Command to be executed
  POC              Windows "ping -n 1 win.REPLACE.server.local"

optional arguments:
  -h, --help       show this help message and exit
  
python Gen-ysoserial-win.py Windows "ping -n 1 win.REPLACE.server.local"
  ```
