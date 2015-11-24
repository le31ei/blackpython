import socket
import threading
import getopt
import sys

def server_listen():
	"""
		-l, --listen 
	"""
	


def usage():
	print "nc Tool"
	print
	print "Usage: nc.py -t target_host -p port"
	print "-l --listen               - listen on [host]:[port] for incoming connection"
	print "-e --excute=file_to_run   - excute the given file upon receiving a connection"
	print "-c --command              - initialize a command shell"
	print "-u --upload=destination   - upload a file"
	print 
	print
	sys.exit(0)


def main():
	if not len(sys.argv[1:]):
		usage()

	try:
		opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",["help","listen","excute","target",\
			"port","command","upload"])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o, a in opts:
		if o in ("-h","--help"):
			usage()
		elif o in ("-l","--listen"):
			server_listen()
	return 0


if __name__ == "__main__":
	main()