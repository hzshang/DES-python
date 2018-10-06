#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 hzshang <hzshang15@gmail.com>
#
# Distributed under terms of the MIT license.

from des import encrypt_des,decrypt_des
def main():
    pt ="hello,world"
    key="12345678"
    ct = encrypt_des(pt,key)
    print "base64(ct):",ct.encode("base64")
    new = decrypt_des(ct,key)
    print "pt:",new
    print "source:",pt

if __name__ == "__main__":
    main()
