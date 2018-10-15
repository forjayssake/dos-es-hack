import anvil.server
#import json

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
elastic_url = 'https://3e20d9de.ngrok.io/'
search_pretty_path = '_search?pretty'

@anvil.server.callable
def call_api():
  data = anvil.http.request('https://3e20d9de.ngrok.io/',json=True)
  return data

@anvil.server.callable
def service_search(search_term, open_only):
  # TODO: open_only
  search_url = str.format("{0}{1}", elastic_url, search_pretty_path)
  print(search_url)
  search_payload = {"query": {"query_string": {"query": search_term}}}
  print(search_payload)
  try:
    response = anvil.http.request(url=search_url,
                    method="POST",
                    data=search_payload,
                    json = True
                    )
    print(response['hits']['total'])
    print(response['hits']['hits'])
    hits = response['hits']
    print(hits['total'])
    return response
  except anvil.http.HttpError as e:
    print("Error %d" % e.content)
#   print(response.error)
  