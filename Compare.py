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
    fout = open("output_Ensemble_Learning_Navigation_system.txt","a")
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

xl=["ensemble","learning refers","multiple learning machines","decision makers","individual predictions","overall accuracy","individual committee menter","numbers class labels posterior probabilities rankings clusterings etc","esemble learning","real world situations","machine learning model","essemble learning","possible decision","overall model selection","classifier lobe","cross valiation 2.","ensemble learning","direuse models 3.","ouy 4.model selection","final goat","risk 5.study","data sample data quantity","train validity test","separate subsets","size use","different bootstrap samples","different classifiers","bootstrap sample","random sample","decision boundary","certain problems","esemble learning","classification system","classifier learns","simpler partitions data fusions","suitable combinations","different source","data fusion data/informations fusion","complementary informations","confidence estimations","decison esemble","high confidence","different decisio esemble","low confidence","high cnfidence","esemble decision","high esemble learning algorithms 1. bagging/bootstrap","bootstarp replicas 2. boostng","creates replicas","informative training data","consecutive classifier","iteration- 3weak classifiers 1. classifiers c1","random subset 2. c2","informative subset","training data","3. c3","c2 disagree","binary class problems ada boost","subset database","sample distributions","classifiers training errors random forests","decision trees","random variables","multicates classification","train /predict","decorate","diverse ensemble creation","artificial training examples","artificial examples","diverse ensembles","combining","ensemble members 1. majority","3. borda"
]

distance_from="Automotive Navigation System"
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