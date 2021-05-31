from nose.tools import *
from Mywindow.Mywindow import Mywindow

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")