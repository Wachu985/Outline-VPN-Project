DEFAULT_SERVER_DATA_LIMIT = 1000 * 1000 * 1000 * 250 #Limite de Transferencia 250 gb

CONVERT_GB = 1000 * 1000 * 1000

import math

def conversor(size_bytes):
   if size_bytes == 0:
       return "0-B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s-%s" % (s, size_name[i])