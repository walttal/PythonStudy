'''

This is to check if IPv4 address is valid 

'''
import IPy
def ipvalidate(ipStr):
#     ip_valid = True
    for i in ipStr.split('.'):
        i = i.lstrip('0')
        if int(i) < 255:
            continue
        else:
#             ip_valid = False
            return False
            break
    return True
    

print ipvalidate('8.43.2.2')
        