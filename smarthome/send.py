from subprocess import Popen
import sys
Popen( ['sshpass', '-p', '00000000', 'scp', 'light_switch.py', 'pi@172.20.10.2:~' ] )
Popen( ['sshpass', '-p', '00000000', 'ssh', 'pi@172.20.10.2', 'python', '~/light_switch.py', sys.argv[1] ] )
