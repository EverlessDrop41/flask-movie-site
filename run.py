from app import server

host = 'localhost'
port = 8080

print ("Running server on http:/{}:{}".format(host, port))
server.run(debug=True, host=host, port=port)
