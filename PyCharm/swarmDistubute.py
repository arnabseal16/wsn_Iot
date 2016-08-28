import os, sys, subprocess, random
fog_ip = []
swarm_ip = []
swarm_usage = []
def fog_Initialize() :
    fo1=open("fog_nodes","r")
    tmp = fo1.read().split("\n")
    for i in range(0,len(tmp)-1) :
        tmp2=tmp[i].split(":")
        fog_ip.append(tmp2[1])
    return
def swarm_Initialize() :
    fo1=open("swarm_nodes_list","r+")
    tmp = fo1.read().split("\n")
    for i in range(0, len(tmp) - 1):
        tmp2 = tmp[i].split(":")
        swarm_ip.append(tmp2[1])
        swarm_usage.append(int(tmp2[2]))
    return
def fog_queue() :
    count = 0
    fo1=open("swarm_nodes","w+")
    fo1.write("node0:")
    capacity = 5000
    for i in range(0,len(swarm_ip)-1) :
        if (swarm_usage[i]>capacity) :
            count=count+1
            if (count>(len(fog_ip)-1)) :
                print "exceeded"
                fo1.write("\n")
                return
            capacity = 2000
            fo1.write("\n")
            fo1.write("node"+str(count)+":")
            fo1.write(swarm_ip[i])
            fo1.write(",")
        else :
            capacity = capacity - int(swarm_usage[i])
            fo1.write(swarm_ip[i]+",")
    fo1.write("\n")
    for i in range(count+1,len(fog_ip)) :
        fo1.write("node"+str(i)+":"+"\n")
    return
fog_Initialize()
swarm_Initialize()
fog_queue()