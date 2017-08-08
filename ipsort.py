

iplist = ['192.168.2.32','192.168.1.21','192.168.1.3','192.168.2.9','10.1.2.3']

iplist.sort(lambda x,y:cmp("".join([i.rjust(3,'0') for i in x.split('.')]), "".join([i.rjust(3,'0') for i in y.split('.')]))) 

print iplist