#FOG_Layer
import os, sys, time, random
fog_nodes = []
bandwdith = []
swarm_nodes = []
def serverInitialize(path) :
    tmp = ""
    if (path == "") :
        print "Path Empty"
        exit(1)
    fo1 = open(path,"r+")
    out = fo1.read()
    global fog_nodes
    fog_nodes = out.split("\n")
    global bandwdith
    for i in range(0,len(fog_nodes)-1):
        bandwdith.append(1000)
    print "The FOG Server Node List:"
    for i in range(0,len(fog_nodes)-1):
        print fog_nodes[i],"::",bandwdith[i]," kbps"

    return


def logger(msg) :
    #subprocess.check_call(['echo',msg,'>>','fog_node_migration.log'])
    #subprocess.call(['echo',msg,'>>','fog_node_migration.log'])
    fo1=open("fog_node_migration.log","a+")
    fo1.write(time.strftime("%c")+"::::"+msg+"\n")
    return

def swarmInitialize() :
    fo1=open("swarm_nodes","r+")
    tmp=fo1.read()
    tmp=tmp.split("\n")
    for i in range(0,len(tmp)-1) :
        numip=tmp[i].split(":")
        tmp[i]=numip[1]
        tmp[i]=tmp[i].split(",")
        logger("Assignment of Nodes to their fog(s) for fog"+str(i))
    del tmp[len(tmp)-1]
    print "Swarm Node Usage List: ", tmp
    return


def fogInitialize() :
    num=int(raw_input("Enter the number of FOG nodes"))
    fo1=open("fog_nodes","w+")
    logger("Received Input for FOG Nodes as " + str(num))
    for i in range(0,num-1) :
        tmp="node"+str(i)+":"+str(i)+str(random.randrange(10,46))+"."+str(random.randrange(0,255))+"."+str(random.randrange(0,255))+"."+str(random.randrange(10,255))
        fo1.write(tmp)
        fo1.write("\n")
        logger("Entries made for fog nodes creation in file fog_nodes"+str(i))
    return

fogInitialize()
serverInitialize(sys.argv[1])
logger("Initialization")
swarmInitialize()

