#muiltprocreeing

import multiprocessing as mul
import subprocess

fr = open("download.txt", "r")
content = fr.readlines()
fr.close()

def f(web):
    subprocess.call(web, shell = True)

pool = mul.Pool(3)
pool.map(f, content)
pool.close()
for sub in pool:
    sub.join()

