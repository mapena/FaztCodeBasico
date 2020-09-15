import subprocess
#subprocess.run(["mkdir", "myfolder"])
#subprocess.run(["ls", "-l"])
#subprocess.run(["mkdir", "-l"],shell=TRUE)  # el comando lo ejecuta sobre el shell
subprocess.run(["mkdir", "-l"],shell=FALSE)  # es lo recomendable para que primero el comando se ejecute en el interprete de python

