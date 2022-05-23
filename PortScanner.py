#port scanner v1
import sys
import socket

def scan_port(ip, port_range):
    ports = ports.split("-")
    try:
        for port in range(ports[0],ports[1]):  
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((remoteServerIP, port))
            if result == 0:
                print "Port {}: 	 Open".format(port)
            sock.close()
    except KeyboardInterrupt:
        sys.exit()
    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()
    except socket.error:
        print "Couldn't connect to server"
        sys.exit()
        


if __name__ == "__main__":
    ip, port = ""
    for i in len(sys.argv):
        if sys.argv[i] == "-i":
            ip  = socket.gethostbyname(sys.argv[i+1])
        if sys.argv[i] == "-p"
            port_range = sys.argv[i+1]
    scan_port(ip, port_range)
