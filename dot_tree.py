def dot_tree(problem):    
   
#pre : a Problem() as input    
#post: Dot graph in string format. Paste this in http://www.webgraphviz.com/ 
#usage: print(dot_tree(problem))  
    root = Node(problem.initial)    
    flatten = lambda l: [item for sublist in l for item in sublist]
    children=[root.child_node(problem, action) for action in problem.actions(root.state)]    
    grandchildren=flatten([[child.child_node(problem, action) for action in problem.actions(child.state)] for child in children])    
    greatgrandchildren=flatten([[child.child_node(problem, action) for action in problem.actions(child.state)] for child in grandchildren])    
    nodes=set(children+grandchildren+greatgrandchildren)
    import pydot    
    
#make a Dot graph of the nodes and connections    
#initial state as double circle     
#goal state is marked with thick lines    
#current implementation only goes two levels down (greatgrandchildren)    
            
    g = pydot.Dot()    
    g.set_type('digraph')    
    g.set_node_defaults(fontname = "helvetica",fontsize=10)    
    g.set_edge_defaults(fontname = "helvetica",fontsize=9)        
    g.add_node(pydot.Node(name=root.state,label='{}'.format(root.state),shape='doublecircle'))    
    for n in nodes:        
        if problem.goal_test(n.state):            
            penwidth=3        
        else:            
            penwidth=1                
        g.add_node(pydot.Node(name=n.state,label='{}'.format(n.state),penwidth=penwidth))    
    for n in nodes:
        g.add_edge(pydot.Edge(n.parent.state,n.state,label='{} ({})'.format(n.action.name,n.action.args)))    
   return g.to_string()



