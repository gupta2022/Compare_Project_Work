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
    fout = open("output_k3_Tablet_Computer.txt","a")
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

xl=["spa requirements","gam station process focus","organisation process definition","software management","agnew ane polk engineering","peer ken ice","spa requirements","level quantitative process management","software quality management spa requirements level","i defect prevention","software company level","india com","dan requirements specification donna king","akin times drama queen canon les","vicious non andre ord","functional view","dynamic view mind seiko function dec","object state ambition","relations diagram","diagram attributes data dictionary data","data press specification","data flow diagram","cam scanner art","employee salary","mary alan data flow diagram process","data flow dalai tow","compute terminator","internal agent process stone","employee sale mat agent employee terminator moo holden","price report pay slip male objects","data flow diagram level","diagram content diagram waste issue info","library infra st supplier schemes","boo les","liable jul ram","ivory book","available limit","search books supplies books","payment return book","fine issue book request","basement issue","boone id enrich","emit tool","available ennis den issue","book mend","i men id exists i member level","return books approach","data flow diagram","classical linen","cam scanner art","ability completeness traceability","consistency details design","una tui quot ness","modify ability semantics","tug sri han capability maturity model com","i duty","auth standards organisation blank software companies kernel","act city spa key process seas","repeatable com","adam hefner","anime lib spa","requirement management","project planning","frost i seasons","software project","i ane sight","subcontract management grad stay module","software quality assurance","configuration management","cam scanner art","time data","diagram event part limit","data event","flow que need","service bacon scenarios events function mange data","monthly weekly trig que","plain dental management","dental service","clos liberia timber thu music","price i","past villas date cd","particular services clinic sends","appointment patient performs","complete re local","smiles doctor","content diagram","note fec","apt hunts patient i digital requests","patient services","ans formation","record clinic","whoitolaitosent keri corset mil art sustain copy moment","patient record","appointment schedule","cam scanner man","time data","date tine","pain ii patient word louis event list","patient record","i click fins","moment request","david i services","goal sentiment patient lent uses rat","patio pats ami click bra vail reg appointment","appointments patient","palate i patients list","dentists i dentists patient days request","patients patients dentist","patriot guards","patient secrets patient records services","cam scanner"
]

distance_from="tablet computer"
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