# -*- coding: utf-8 -*-
import datetime
from http.server import HTTPServer
from HTTPRequestHandler import HTTPRequestHandler
import  sett

def run(server_class=HTTPServer, handler_class=HTTPRequestHandler):
    handler_class.server_version = "IA"
    handler_class.sys_version = "0.1"
    server_address = ( sett.host, sett.port )
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    print("Start at {date}".format(date=datetime.datetime.now()))
    run()