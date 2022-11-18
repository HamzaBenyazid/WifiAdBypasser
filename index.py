#!/usr/bin/python3

from WifiAdBypasser import WifiAdBypasser
import argparse

# read bypassByClassAndIndex arguments from command line with argparse
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--gatewayIp",
                    help="gateway ip address", default="http://192.168.1.1")
parser.add_argument("-v", "--videoElementClass",
                    help="video element class name", default="mejs-overlay-button")
parser.add_argument("-i", "--index", help="video element index", default=0)
parser.add_argument("-l", "--videoLength", help="video length", default=30)
args = parser.parse_args()

# create an instance of WifiAdBypasser
bypasser = WifiAdBypasser()

# bypass the public wifi ad
bypasser.bypassByClassAndIndex(
    gatewayIp=args.gatewayIp,
    videoElementClass=args.videoElementClass,
    index=args.index,
    videoLength=args.videoLength
)