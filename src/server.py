import sys, subprocess

def print_usage():
    usage = "Usage: python server.py [congestion control option] [args]"
    default_tcp = "  Default TCP: python server.py TCP PORT"
    print usage
    print "Examples:"
    print default_tcp

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    cc_option = sys.argv[1]
    if cc_option.lower() == 'tcp':
        cmd = ['./tcpserver']
        if len(sys.argv) >= 3:
            cmd += sys.argv[2:]
        subprocess.call(cmd, cwd='../external/sourdough/examples')
    
if __name__ == '__main__':
    main()
