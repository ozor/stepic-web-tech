from cgi import parse_qs

def wsgi_application(environ, start_response):

  query = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
  body = []
  for key, values in query.items():
    for item in values:
      body.append(key + "=" + item + "\n")
   
  status = '200 OK'
  headers = [
   ('Content-Type', 'text/plain')
  ]
  
  start_response(status, headers)
  return body
