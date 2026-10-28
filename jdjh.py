def dir_bruter(word_queue,extensions=None):
  while not word_queue.empty():
    attempt = word_queue.get()
    attempt_list = []
    
    # check to see if there is a file extension; if not,
    # it's a directory path we're bruting
    
    if "." not in attempt:
      attempt_list.append("/%s/" % attempt)
    else:
      attempt_list.append("/%s" % attempt)
      # if we want to bruteforce extensions
    if extensions:
      for extension in extensions:
        attempt_list.append("/%s%s" % (attempt,extension))
        # iterate over our list of attempts
    for brute in attempt_list:
      url = "%s%s" % (target_url,urllib.quote(brute))
      try:
      
      headers = {}
      headers["User-Agent"] = user_agent
      r = urllib2.Request(url,headers=headers)
      response = urllib2.urlopen(r)
      
      if len(response.read()):
      print "[%d] => %s" % (response.code,url)
    except urllib2.URLError,e:
      if hasattr(e, 'code') and e.code != 404:
      print "!!! %d => %s" % (e.code,url)
    pass
