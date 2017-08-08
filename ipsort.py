


iplist.sort(lambda x,y:cmp("".join([i.rjust(3,'0') for i in x.split('.')]), "".join([i.rjust(3,'0') for i in y.split('.')]))) 