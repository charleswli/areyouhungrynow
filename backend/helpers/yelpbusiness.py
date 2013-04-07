import json
import oauth2
import optparse
import urllib
import urllib2
import yelpkeys

def request(business_id):
  consumer_key = yelpkeys.CONSUMER_KEY
  consumer_secret = yelpkeys.CONSUMER_SECRET
  token = yelpkeys.TOKEN
  token_secret = yelpkeys.TOKEN_SECRET

  host = 'api.yelp.com'
  url_params = {}
  path = '/v2/business/%s' % (business_id,)

  """Returns response for API request."""
  # Unsigned URL
  encoded_params = ''
  if url_params:
    encoded_params = urllib.urlencode(url_params)
  url = 'http://%s%s?%s' % (host, path, encoded_params)
  #  print 'URL: %s' % (url,)

  # Sign the URL
  consumer = oauth2.Consumer(consumer_key, consumer_secret)
  oauth_request = oauth2.Request('GET', url, {})
  oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                        'oauth_timestamp': oauth2.generate_timestamp(),
                        'oauth_token': token,
                        'oauth_consumer_key': consumer_key})

  token = oauth2.Token(token, token_secret)
  oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
  signed_url = oauth_request.to_url()
  #  print 'Signed URL: %s\n' % (signed_url,)

  # Connect
  try:
    conn = urllib2.urlopen(signed_url, None)
    try:
      response = json.loads(conn.read())
    finally:
      conn.close()
  except urllib2.HTTPError, error:
    response = json.loads(error.read())

  return response

#response = request(options.host, path, url_params, options.consumer_key, options.consumer_secret, options.token, options.token_secret)
#print json.dumps(response, sort_keys=True, indent=2)
