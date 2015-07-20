#!/usr/bin/env python
""" test_public_key.py

    Copyright (c) 2015 by Paul A. Lambert   
"""
import unittest

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    p = path.abspath(__file__)  # ./cryptopy/persona/test/test_cipher_suite.py
    for i in range(4):  p = path.dirname( p )   # four levels down to project '.'
    sys.path.append( p )
    
from cryptopy.persona.public_key import PublicKey, PublicKeyPair
from cryptopy.persona.cipher_suite import Suite_01

    
class TestPublicKey(unittest.TestCase):
    """  """
    def test_basic_pk(self):
        """ Basic unit test of a PublicKey Pair """
        cipherSuite = Suite_01()
        curve = cipherSuite.Group()
        point = 55555555555555555555555555 * curve.generator()
        print curve.generator()
        
        pubKey = PublicKey( cipherSuite, point )
   
        
class TestPublicKeyPair(unittest.TestCase):
    """  """
    def test_basic(self):
        """ Basic unit test of a PublicKey Pair """
        cipherSuite = Suite_01()
        keyPair1 = PublicKeyPair( cipherSuite )
        keyPair2 = PublicKeyPair( cipherSuite )



if __name__ == '__main__':
    unittest.main()
