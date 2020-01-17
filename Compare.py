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
    fout = open("output_k2_Electronic_Instruments.txt","a")
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

xl=["requirements solicitation traceability","proper documentation","requirement meeting","large co miles","system user customer","sri software requirements specification","sri formats","tut seduction til repose","scope wall","definitions acronyms abbreviation com","references legacy systems","overview com","overall description","product perspective","product functions","characteristics ii music","dependencies com","functional req party requirements","anime reg","specific requirement","design constraints","time citation internet","porn analysis","domain analysis","task analysis","user scenario ethnography use case reg limitation matter","observe commons","delphi technique","raw discussion problem moment","i group discussion","side talk analysis","tasks hierarchical structure forum analysis","account data","domain analysis ada law legacy systems","user scenario i use case","req limitation","rate story","light sequence","alternate steps","wrong basal sin","cam scanner linear sea","pure prot","increment increment","complete product","i cement","blow end","parts spinal model planning bit probability","failure analysis","inner communication project gain","point customer valuation construction","customer comm risk analysis release","evolutionary iterative","complex doc diff","systematic tim ear seq model","cam scanner art","informal set i","formal sea sri","seq software requirement specifics","red requirement specification requirements","condition capability","condition i capability","system i","system component","standard specification","condition i capability","fees non function","syst domain i","equine rent","cults domain","i requirement process","req limitation gathering","reg specification representation","charts diagrams","validation validation","diag rains","errors propagation","cam scanner art","time rad","rapid action development","short span quality compromise","suitable agile software development","strict rigid rule","pen requirement","resource availability","documentation scrum","equal model","requirements analysis demands desire","requirement analysis good quality","product requirements analysis results","software operational characteristics","function data","software interface","system elements","software designer","tia function","data architectural interface","component level designs","i problem recognition","evaluation synthesis feasibility","specification man data","cam scanner"
]

distance_from="Electronic Instrument"
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