from gevent.pywsgi import WSGIServer

from src import create_app
from src.env import env
from src.logger import logger

print(env)

if __name__ == "__main__":
    application = create_app()

    if env.DEBUG:
        application.run(debug=True, host="0.0.0.0", port=env.PORT)
    else:
        srv = WSGIServer(("0.0.0.0", env.PORT), application, log=logger)
        srv.serve_forever()
