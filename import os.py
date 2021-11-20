import os
import shutil
path = '/C:Users/prasa/'
print("before moving file:")
print(os.list(path))
source = "/C:Users/prasa/test.txt"
destination = "/C:Users/prasa/test(copy).txt"
dest = shutil.move(source,destination)
