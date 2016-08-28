import os, sys, subprocess, random, time
swarm_usage = []
swarmip = []
def initialize(num) :
    for i in range(0,num-1) :
        swarm_usage.append(int(random.randrange(0,255)))
        swarmip.append(str(random.randrange(170,255)) +"."+ str(random.randrange(10,255)) +"."+ str(random.randrange(10,255)) +"."+ str(random.randrange(10,255)))
        print swarm_usage[i],":",swarmip[i]
        logger(str(i)+" node created for ip"+swarmip[i]+"with usage bandwidth"+str(swarm_usage[i]))
    return
def inputFile() :
    fo1=open("swarm_nodes_list","w+")
    for i in range(0,len(swarmip)-1) :
        fo1.write("node"+str(i)+":"+swarmip[i]+":"+str(swarm_usage[i]))
        fo1.write("\n")
    logger("Node data piped to file"+"swarm_nodes_list")
    return
#subprocess.check_call(['cat','swarm_nodes_list'])
def logger(msg) :
    #subprocess.check_call(['echo',msg,'>>','fog_node_migration.log'])
    #subprocess.call(['echo',msg,'>>','fog_node_migration.log'])
    fo1=open("fog_node_migration.log","a+")
    fo1.write(time.strftime("%c")+"::::"+msg+"\n")
    return
initialize(int(raw_input("Enter the number of nodes")))
inputFile()
