from http.server import BaseHTTPRequestHandler
import urllib.parse
import os.path

def read_file_to_str(filename):
    t = open( filename, "rb" )
    return t.read()

class HTTPRequestHandler( BaseHTTPRequestHandler ):
    """docstring for HTTPRequestHandler"""
    def ans_like_text_file( self, filename, contenttype ):
        if os.path.isfile( filename ):
            self.send_response(200)
            self.send_header( "Content-type", contenttype )
            self.send_header( "cache-control", "public, max-age=86400" )
            self.end_headers()
            bs = read_file_to_str( filename )
            self.wfile.write( bs )
    def ans_like_text( self, html ):
            self.send_response(200)
            self.send_header( "Content-type", "text/html" )
            self.end_headers()
            bs = bytearray( html, "utf-8" )
            self.wfile.write( bs )
    def ans_like_304( self ):
            self.send_response(304)
            self.end_headers()
    def ans_like_404( self ):
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            bs = read_file_to_str( "html/404.html" )
            self.wfile.write( bs )
    def get_postdata( self ):
        self.send_response(200)
        self.send_header( "Content-type", "application/json" )
        self.end_headers()
        length = int( self.headers[ "Content-Length" ] )
        res = urllib.parse.parse_qs( self.rfile.read( length ).decode( "utf-8" ) )
        return res
    def do_GET( self ):
        o = urllib.parse.urlparse( self.path )
        path = o.path
        #print( self.headers._headers[0][1] )
        if True:
            if (path.find('..')==-1):
                if path == "/":
                    self.ans_like_text_file( "html/index.html", "text/html" )
                elif path[ -5: ] == ".html":
                    self.ans_like_text_file( "html/" + path[ 1: ], "text/html" )
                elif path[ -3: ] == ".js":
                    self.ans_like_text_file( "js/" + path[ 1: ], "text/javascript" )
                elif path[ -4: ] == ".css":
                    self.ans_like_text_file( "css/" + path[ 1: ], "text/css" )
                elif path[ -4: ] == ".ico":
                    self.ans_like_text_file( "image/" + path[ 1: ], "image/ico" )
                elif path[ -4: ] == ".png":
                    self.ans_like_text_file( "image/" + path[ 1: ], "image/png" )
                elif path[ -4: ] == ".svg":
                    self.ans_like_text_file( "image/" + path[ 1: ], "image/svg+xml" )
                else:
                    self.ans_like_404()
            else:
                self.ans_like_404()