from optparse import OptionParser
parser = OptionParser()
parser.add_option("-u", "--user", dest="username", help="username string", metavar="USERNAME_STRING")
parser.add_option("-g", "--group", dest="usergroup", help="usergroup string", metavar="USERGROUP_STRING")
parser.add_option("-4", "--ipv4", dest='ipv4', action='store_true', metavar="CHECK_IPV4")

(options, args) = parser.parse_args()
if options.ipv4:
    print 'Haha'

required = "username usergroup".split()
for r in required:
    if options.__dict__[r] is None:
        parser.error("parameter %s required" % r)

print options
#options --> class instance
#args --> list
