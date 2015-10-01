# -*- coding: utf-8 -*-
import os
import datetime
from http.server import HTTPServer
from Server.myhttpd.HTTPRequestHandler import HTTPRequestHandler
import Server.sett as sett
import Server.common as common
import projectorium.reloader
import projectorium.rerender
import dbclasses.dbworker
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential(sett)

def run(server_class=HTTPServer, handler_class=HTTPRequestHandler):
    handler_class.server_version = "IA1"
    handler_class.sys_version = "0.1"
    server_address = ( sett.host, sett.port )
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    common.detect_common_env()
    print("Start at {date}".format(date=datetime.datetime.now()))
    run()