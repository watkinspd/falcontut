# examples/things.py

# Let's get this party started!
from wsgiref.simple_server import make_server

import falcon
import os


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nHello friends! \n'
                    'This is the text that is returned '
                     'from the http get method.\n'
                     '\n'
                     '    ~ The demo app\n\n')


# falcon.App instances are callable WSGI apps
# in larger applications the app is created in a separate file
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/things', things)
app.add_route('/', things)

port = int(os.environ.get(PORT, '8050'))

if __name__ == '__main__':
    with make_server('', port, app) as httpd:
        print('Serving on port '.format(port))

        # Serve until process is killed
        httpd.serve_forever()