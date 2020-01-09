from collections import defaultdict

def addEdge(graph,u,v):
    graph[u].append(v)

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges
# displaying all values for a key in the graph

def show_edges(graph):
    edges=generate_edges(graph)
    for n in edges:
     print (n)


def find_shortest_path(graph, start, end, path =[]):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
def add_to_file(graph,name):
    open("created_graph/"+name+".txt", 'w').close()
    fout = open("created_graph/"+name+".txt","w")
    for node in graph:
        fout.write(node)
        fout.write("\n")
        for neighbour in graph[node]:
            fout.write(neighbour)
            fout.write("\n")
        fout.write("-1\n")
    fout.write("-2\n")

def output_file(query,gname,path):
    fout = open("outputk1_Ultrasound.txt","a")
    fout.write(query)
    fout.write("\n")
    fout.write(gname)
    fout.write("\n")
    #for node in path:
     #   fout.write(node)
      #  fout.write("\n")

    fout.write(str(len(path)))
    fout.write("\n")
    fout.write("-1\n")

def read_from_file(graph,name):
    try:
        fin = open("Created_Graph/"+name+".txt",encoding="utf8")
    except :
        return 0
    query=fin.readline()
    query=query.replace("\n","")
    while(query and query!="-2"):
        val=fin.readline()
        val=val.replace("\n","")
        while(val and val!="-1"):
            addEdge(graph,query,val)
            val=fin.readline()
            val=val.replace("\n","")
        query=fin.readline()
        query=query.replace("\n","")
    return 1

graph = defaultdict(list)

xl=["problem domain","app implementation","spiral model","defence aeronautics","customer requirements analysis","requirement need","customers stakeholders","party i","requirement requirements document","informal sri","red software requirement specification requirements specification document output","software operational","functional data","software interface","system elements","soft core design sex","information function","data architecture interface","component level designs","cam scanner","rabid action development model","major constraint","detail agile software development","dean documentation","customer interaction","daily basis","techniques scrum","detail ftp","small scale software check gucci","cam scanner","library waterfall","bugs bug identification","big business spiral model planning risk analysis customer communication engineering project","point customer evaluation construction","evolutionary iterative","systematic dover linear","release sequential mode risk analysis","cam scanner risk feat","poses threat","successful completion","software cost time govt policies requirements","large projects","suck analysis predictability","future technology","prot tin","incremental model","interface linear","word processing","basic wood processing functions","complete set","cost time","combination advantages dis adv case documentation customer feedback i","requirements improvement","modules i need","available users","advance bugs","teams partial dak","cam scanner","model class","rise customer test devices","large complex projects","partial requirements","customers advice time","developer customer","system analyst","nascent iterations co prom","minor fixes","land sic","customer quality","tit dos","cam scanner"
]

distance_from="ultrasound machine"
read_from_file(graph,distance_from)
ans=[]
for query in xl :
    del ans [:]
    ans=[]
    graph2 = defaultdict(list)
    x=read_from_file(graph2,query)
    cd = query
    f=0
    for ab in graph:
        for xe in graph2:
            #print (ab + "  ------- "+xe)
            if ab == xe :
                if f==0:
                    f=1
                    output_file(query,distance_from,[])