from graphviz import Digraph
from graphviz import Source
gra = Digraph()

#initial state
gra.node('s','',color='white')
gra.node('s0', 's0',shape='circle')
gra.edge('s','s0')

#states for words starting with 'a'
gra.node('s1', 's1',shape='circle')
gra.node('s2', 's2',shape='circle')
gra.node('s3','s3',shape='doublecircle')
gra.node('s4', 's4',shape='circle')
gra.node('s5', 's5',shape='circle')
gra.node('s6', 's6',shape='circle')
gra.node('s7','s7',shape='doublecircle')

#reject States
gra.node('r', 'Reject',shape='circle')
gra.node('r1', 'Reject',shape='circle')
gra.node('r2', 'Reject',shape='circle')
gra.node('r3', 'Reject',shape='circle')
gra.node('r4', 'Reject',shape='circle')
gra.node('r5', 'Reject',shape='circle')
gra.node('r6', 'Reject',shape='circle')


#edge of first letter 'a'
gra.edge('s0','s1','a|A')

#"and" edges
gra.edge('s1','s2','n|N')
gra.edge('s2','s3','d|D')

#"array" edges
gra.edge('s1','s4','r|R')
gra.edge('s4','s5','r|R')
gra.edge('s5','s6','a|A')
gra.edge('s6','s7','y|Y')

#reject edges for words starting with 'a'
gra.edge('s1','r','[a-m]|[A-M]|[o-q]|[O-Q]|[s-z]|[S-Z]')
gra.edge('s2','r','[a-c]|[A-c]|[e-z]|[E-Z]')
gra.edge('s3','r','[a-z]|[A-Z]')
gra.edge('s4','r1','[a-q]|[A-Q]|[s-z]|[S-Z]')
gra.edge('s5','r1','[b-z]|[B-Z]')
gra.edge('s6','r1','[a-x]|[A-X]|z|Z')
gra.edge('s7','r1','[a-z]|[A-Z]')

#states for words starting with 'b'
gra.node('s8', 's8',shape='circle')
gra.node('s9', 's9',shape='circle')
gra.node('s10', 's10',shape='circle')
gra.node('s11', 's11',shape='circle')
gra.node('s12','s12',shape='doublecircle')

#edge for start letter 'b'
gra.edge('s0','s8','b|B')

#"begin" edges
gra.edge('s8','s9','e|E')
gra.edge('s9','s10','g|G')
gra.edge('s10','s11','i|I')
gra.edge('s11','s12','n|N')

#reject edges for words starting with 'b'
gra.edge('s8','r2','[a-d]|[A-D]|[f-z]|[F-Z]')
gra.edge('s9','r2','[a-f]|[A-F]|[h-z]|[H-Z]')
gra.edge('s10','r2','[a-h]|[A-H]|[j-z]|[J-Z]')
gra.edge('s11','r2','[a-m]|[A-M]|[o-z]|[O-Z]')
gra.edge('s12','r2','[a-z]|[A-Z]')

#node for start letter 'c'
gra.node('s13', 's13',shape='circle')

#nodes for words starting with 'c'
gra.node('s14', 's14',shape='circle')
gra.node('s15', 's15',shape='circle')
gra.node('s16', 's16',shape='circle')
gra.node('s17', 's17',shape='circle')
gra.node('s18', 's18',shape='circle')
gra.node('s19', 's19',shape='doublecircle')

#edge for start letter 'c'
gra.edge('s0','s13','c|C')

#"case" edges
gra.edge('s13','s14','a|A')
gra.edge('s14','s15','s|S')
gra.edge('s15','s19','e|E')

#"const" edges
gra.edge('s13','s16','o|O')
gra.edge('s16','s17','n|N')
gra.edge('s17','s18','s|S')
gra.edge('s18','s19','T|t')

#reject edges for words starting with 'c'
gra.edge('s13','r3','[b-n]|[B-N]|[p-z]|[P-Z]')
gra.edge('s14','r3','[a-r]|[A-R]|[t-z]|[T-Z]')
gra.edge('s15','r3','[a-d]|[A-D]|[f-z]|[F-Z]')
gra.edge('s16','r4','[a-m]|[A-M]|[o-z]|[O-Z]')
gra.edge('s17','r4','[a-r]|[A-R]|[t-z]|[T-Z]')
gra.edge('s18','r4','[a-s]|[A-S]|[u-z]|[U-Z]')
gra.edge('s19','r4','[a-z]|[A-Z]')

#node for start letter 'd'
gra.node('s20', 's20',shape='circle')

#edge for start letter 'd'
gra.edge('s0','s20','d|D')

#nodes for words starting with 'd'
gra.node('s21', 's21',shape='circle')
gra.node('s22', 's22',shape='doublecircle')
gra.node('s23', 's23',shape='circle')
gra.node('s24', 's24',shape='circle')
gra.node('s25', 's25',shape='circle')
gra.node('s26', 's26',shape='doublecircle')

#"do" edges
gra.edge('s20','s22','o|O')

#"div" edges
gra.edge('s20','s21','i|I')
gra.edge('s21','s26','v|V')

#"downto" edges
gra.edge('s22','s23','w|W')
gra.edge('s23','s24','n|N')
gra.edge('s24','s25','t|T')
gra.edge('s25','s26','o|O')

#reject edges for words starting with 'd'
gra.edge('s20','r5','[a-h]|[A-H|[j-n]|[J-N]|[p-z]|[P-Z]')
gra.edge('s21','r5','[a-u]|[A-U]|[w-z]|[W-Z]')
gra.edge('s22','r5','[a-v]|[A-V]|[x-z]|[X-Z]')
gra.edge('s23','r5','[a-m]|[A-M]|[o-z]|[O-Z]')
gra.edge('s24','r5','[a-s]|[A-S]|[u-z]|[U-Z]')
gra.edge('s25','r5','[a-n]|[A-N]|[p-z]|[P-Z]')
gra.edge('r5','r5','[a-z]|[A-Z]')
gra.edge('s26','r5','[a-z]|[A-Z]')

#node for start letter 'd'
gra.node('s27', 's27',shape='circle')

#edge for start letter 'e'
gra.edge('s0','s27','e|E')

#nodes for words starting with 'e'
gra.node('s28', 's28',shape='circle')
gra.node('s29', 's29',shape='circle')
gra.node('s30', 's30',shape='circle')
gra.node('s31', 's31',shape='doublecircle')

#"else" edges
gra.edge('s27','s28','l|L')
gra.edge('s28','s29','s|S')
gra.edge('s29','s31','e|E')

#"end" edges
gra.edge('s27','s30','n|N')
gra.edge('s30','s31','d|D')

#reject edges for words starting with 'e'
gra.edge('s27','r6','[a-k]|[A-K]|m|M|[n-z]|[N-Z]')
gra.edge('s28','r6','[a-r]|[A-R]|[t-z]|[T-Z]')
gra.edge('s29','r6','[a-d]|[A-D]|[f-z]|[F-Z]')
gra.edge('s30','r6','[a-c]|[A-C]|[e-z]|[E-Z]')
gra.edge('r6','r6','[a-z]|[A-Z]')
gra.edge('s31','r6','[a-z]|[A-Z]')

gra


