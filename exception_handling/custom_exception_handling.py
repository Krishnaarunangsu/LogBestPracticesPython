# Simple Custom Exception
class UnderLimit(Exception):
    pass

def verify_limit(limit: object) -> object:
   """
   :param limit: object
   :rtype: object
   """
   if int(limit) < 18:
       raise UnderLimit
   else:
       print('Limit: '+str(limit))


# main program
verify_limit(23)  # won't raise exception
verify_limit(17)  # will raise exception
