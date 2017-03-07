# coding:utf-8
from SimpleXMLRPCServer import SimpleXMLRPCServer


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


server = SimpleXMLRPCServer(("localhost", 8000))
print "listening on 8000"
server.register_multicall_functions()
server.register_function(add, "add")
server.register_function(subtract, "subtract")


