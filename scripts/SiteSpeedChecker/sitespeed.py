import socket, time, urllib, urlparse,optparse

def decideFunctionName(URL):
    urlinfo = urlparse.urlparse(URL)

    start = time.time()
    ip = socket.gethostbyname( urlinfo.netloc )
    dns_tm = time.time()-start
    print 'DNS:\t\t{:.3f} seconds'.format( dns_tm )

    start = time.time()
    _data = urllib.urlopen(URL).read()
    load_tm = time.time()-start
    print 'load:\t\t{:.3f} seconds'.format( load_tm )
    print 'w/o DNS:\t{:.3f} seconds'.format( load_tm-dns_tm )



def main():
    usage       = '''%prog [-h] [-v] [-u "url"]'''
    version     = "%prog version 1.0"
    description = 'A cross-platform python based utility to check load time of websites.'
    parser = optparse.OptionParser(usage=usage,version=version,conflict_handler="resolve", description=description)
    general = optparse.OptionGroup(parser, 'General')
    general.add_option(
            '-h', '--help',
            action='help',
            help='Shows the help and exit.')
    general.add_option(
            '-v', '--version',
            action='version',
            help='Shows the version and exit.')
    target = optparse.OptionGroup(parser, "Target")
    target.add_option(
            "-u", "--url", 
            action='store_true',
            dest='web',\
            help="Target website to check.")
    parser.add_option_group(general)
    parser.add_option_group(target)
    (options, args) = parser.parse_args()
    if not options.web:
        parser.print_help()
    elif options.web:
        url = args[0]
        decideFunctionName(url)


if __name__ == '__main__':
    main()
