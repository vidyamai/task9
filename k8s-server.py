#!/usr/bin/python3

import cgi
import subprocess as sp

print("content-type: text/html")
print("Access-Control-Allow-Origin:*")
print()

cmd = cgi.FieldStorage().getvalue("x")
n = cgi.FieldStorage().getvalue("n") #n will mostly have the name
a = cgi.FieldStorage().getvalue("a") #a will take extra arguments 


# get pods deploy svc rc
if ("show" in cmd or "list" in cmd or "display" in  cmd) and ("deploy" in cmd or "deployment" in cmd or "pod" in cmd or "container" in cmd or "svc" in cmd or "service" in cmd or "rc" in cmd):
    if ("deploy" in cmd or "deployement" in cmd):
        op = sp.getoutput("sudo kubectl get deployment")  #list deployment

    elif ("pod" in cmd or "containers" in cmd or "pods" in cmd):
        op = sp.getoutput("sudo kubectl get pods")  #list pods.

    elif ("rc" in cmd):
        op = sp.getoutput("sudo kubectl get rc") # list rc

    else:
        op = sp.getoutput("sudo kubectl get svc") # list svc

# create pods deploy

elif ("create" in cmd or "launch" in cmd or "build" in cmd ) and ("deployment" in cmd or "deploy" in cmd or "pod" in cmd or "container" in cmd):
    if ("deployment" in cmd or "deploy" in cmd):
        op = sp.getoutput(f"sudo kubectl create deployment {n} --image={a}") #create deployment

    else:
        op = sp.getoutput(f"sudo kubectl run {n} --image={a}")  #create a pod

# get nodes
elif ("list" in cmd or "show" in cmd or "display" in cmd) and ("nodes" in cmd):
    op = sp.getoutput("sudo kubectl get nodes")

# kubectl expose deployment pods
elif ("expose" in cmd or "disclose" in cmd or "create" in cmd) and ("pods"in cmd or "pod" in cmd or "container" in cmd or "deploy" in cmd or "deployment" in cmd or "loadbalancer" in cmd) :
    if ("deployment" in cmd or "deploy" in cmd):
        op = sp.getoutput(f"sudo kubectl expose deployment {n} --port={a} --type=NodePort")

    else:
        op = sp.getoutput(f"sudo kubectl expose pod {n} --port={a} --type=NodePort")

# scale the deployment
elif ("create" in cmd or "scale" in cmd or "replicate" in cmd) and ("deploy" in cmd or "deployment" in cmd or "replica" in cmd or "replicas" in cmd):
    op = sp.getoutput(f"sudo kubectl scale deployment {n} --replicas={a}")

# delete the pod deploy svc
elif ("delete" in cmd or "remove" in cmd ) and ("deploy" in cmd or "deployment" in cmd or "pod" in cmd or "container" in cmd or "svc" in cmd or "service" in cmd):

    if ("deploy" in cmd or "deployement" in cmd):
        op = sp.getoutput(f"sudo kubectl delete deployment {n}")

    elif ("pod" in cmd or "pods" in cmd or "container" in cmd):
        op = sp.getoutput(f"sudo kubectl delete pod {n} ")

    else:
        op = sp.getoutput(f"sudo kubectl delete svc {n} ")

# delete entire infrastructure
elif ("delete" in cmd or "remove" in cmd or "destroy" in cmd  or "clean" in cmd) and ("infrastructure" in cmd or "all" in cmd or "environment" in cmd):
    op = sp.getoutput("sudo kubectl delete all --all")

else:
    print("Your requirement is not satisfied !")

print("<pre>")
print("<b>")
print(op)
print("</b>")
print("</pre>")