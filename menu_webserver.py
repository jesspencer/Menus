from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi


#import CRUD operations from database_setup.py
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#code that creates the database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
#code that creates the session is imported from menuAdds.py
DBSession = sessionmaker(bind = engine)
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            #new if statement
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += '<html><body>'
                #add for statement
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>" # br means break the line
                    output += "<a href = '#' > Edit </a>"
                    output += "</br>"
                    output += "<a href = '#' > Delete </a>"
                    output += "</br></br></br>"

                output += "</body></html>"
                self.wfile.write(output)
                return

        except IOError:
            self.send_error(404,"File not Found %s" % self.path)

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s " % port
        server.serve_forever()
    except KeyboardInterrupt:
        print "^C entered, stopping sever ..."
        server.socket.close()




if __name__ =='__main__':
    main()
