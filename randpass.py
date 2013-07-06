#!/usr/bin/python

import random
import string
import argparse



def password():
    parser = argparse.ArgumentParser(description='Create Random Passsword')
    parser.add_argument('-n', action='store_const', const=True, default=False, help='use numbers?')
    parser.add_argument('-u', action='store_const', const=True, default=False, help='use uppercase?')
    parser.add_argument('-l', action='store_const', const=True, default=False, help='use lowercase?')
    parser.add_argument('-s', help='use these symbols', default="")
    parser.add_argument('length', metavar='N', nargs='?', help='length of password', type=int)

    args = parser.parse_args()
    bits = ''
    if args.s:
        sbits = ''
        while len(sbits) < 26:
            sbits += args.s
        bits += sbits
    if args.n:
        nbits = ''
        while len(nbits)<26:
            nbits += string.digits
        bits += nbits
    if args.u:
        ubits = ''
        while len(ubits) < 26:
            ubits += string.ascii_uppercase
        bits += ubits
    if args.l:
        lbits = ''
        while len(lbits) < 26:
            lbits += string.ascii_lowercase
        bits += lbits
    
    if args.length:
        if len(bits)==0:
            print "-----"
        else:
            print ''.join(random.choice(bits) for x in xrange(args.length))

if __name__=='__main__':
    password()
