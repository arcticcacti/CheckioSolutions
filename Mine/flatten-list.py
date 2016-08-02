# "Flatten a list" downloaded: Sun Jul 31 18:31:06 2016
def g(a):
 for i in a:
  try:
   for j in g(i):
    yield j
  except TypeError:
   yield i

def flat_list(a):
 return [x for x in g(a)]

