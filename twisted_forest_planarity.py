#!python

import planarity


DETAILED_VERTICES = set([
    # twisted path
    # 1-2-3-4-5
    'tp1-1', 'tp1-2', 'tp1-3', 'tp1-4', 'tp1-5',
    'tp2-1', 'tp2-2', 'tp2-3', 'tp2-4', 'tp2-5',
    'tp3-1', 'tp3-2', 'tp3-3', 'tp3-4', 'tp3-5',
    'tp4-1', 'tp4-2', 'tp4-3', 'tp4-4', 'tp4-5',
    'tp5-1', 'tp5-2', 'tp5-3', 'tp5-4', 'tp5-5',

    # crossroads
    # 1-2-3
    #
    # 4-5-6-7
    'cr1-1', 'cr1-2', 'cr1-3', 'cr1-4', 'cr1-5', 'cr1-6', 'cr1-7',
    'cr2-1', 'cr2-2', 'cr2-3', 'cr2-4', 'cr2-5', 'cr2-6', 'cr2-7',
    'cr3-1', 'cr3-2', 'cr3-3', 'cr3-4', 'cr3-5', 'cr3-6', 'cr3-7',

    # bent tree
    # 1-+ 2
    #   3
    # 4-+-5
    'bt-1', 'bt-2', 'bt-3', 'bt-4', 'bt-5',

    # haunted house
    # 1---2
    'hh-1', 'hh-2',

    # phantom road
    #  5
    # /
    # 4--3
    #     \
    # 1----2 
    'pr-1', 'pr-2', 'pr-3', 'pr-4', 'pr-5', 

    # haunted ? (map name obscured and I'm too lazy to look it up)
    #   2
    #   |
    # 1-+-3
    'h?-1', 'h?-2', 'h?-3',
    
    # swamp bog
    # 1 -- 2
    'sb-1', 'sb-2',
    
    # forgotten path
    # 1---+
    #     |
    # 2---+
    # 3-4-5
    'fp-1', 'fp-2', 'fp-3', 'fp-4', 'fp-5',

    # dead man's gorge
    # 1       5
    #   2-3-4
    'dmg-1', 'dmg-2', 'dmg-3', 'dmg-4', 'dmg-5',
])

# all edges specified alphabetically
# edges are specified twice (once for each vertex) for error-checking later
INTER_MAP_EDGES = [
    # haunted house
    ('bt-4', 'hh-2'), ('hh-1', 'sb-2'),
    # bent tree
    ('bt-3', 'cr1-6'), ('bt-1', 'dmg-3'), ('bt-5', 'h?-1'),
    ('bt-4', 'hh-2'), ('bt-2', 'cr2-4'),
    # dead man's gorge
    ('bt-1', 'dmg-3'), ('dmg-2', 'tp1-3'),
    ('dmg-1', 'fp-5'), ('dmg-4', 'tp4-2'), ('dmg-5', 'tp4-4'),
    # swamp bog
    ('cr1-7', 'sb-1'), ('cr2-7', 'sb-1'), ('hh-1', 'sb-2'),
    # haunted ?
    ('cr1-2', 'h?-2'), ('bt-5', 'h?-1'), ('cr2-4', 'h?-3'),
    # phantom road
    ('pr-1', 'tp2-1'), ('pr-2', 'tp3-5'), ('cr3-4', 'pr-5'),
    # forgotten path
    ('cr3-1', 'fp-2'), ('fp-3', 'tp4-3'), ('cr2-3', 'fp-4'), ('dmg-1', 'fp-5'),
    # twisted path 1
    ('tp1-1', 'tp2-2'), ('cr2-6', 'tp1-2'), ('dmg-2', 'tp1-3'),
    ('cr1-5', 'tp1-4'), ('tp1-5', 'tp2-4'), ('cr2-1', 'tp1-5'),
    # twisted path 2
    ('pr-1', 'tp2-1'), ('tp2-2', 'tp3-4'), ('cr1-1', 'tp2-2'),
    ('tp1-1', 'tp2-2'), ('tp2-3', 'tp3-2'), ('cr2-2', 'tp2-3'), ('cr2-5', 'tp2-3'),
    ('cr3-5', 'tp2-4'), ('tp1-5', 'tp2-4'), ('cr1-5', 'tp2-5'), ('tp2-5', 'tp5-5'),
    # twisted path 3
    ('cr1-4', 'tp3-1'), ('tp3-2', 'tp5-1'), ('tp2-3', 'tp3-2'), ('cr2-6', 'tp3-3'),
    ('tp2-2', 'tp3-4'), ('cr1-3', 'tp3-4'), ('cr3-3', 'tp3-5'), ('pr-2', 'tp3-5'),
    # twisted path 4
    ('cr3-6', 'tp4-1'), ('tp4-2', 'tp5-4'), ('dmg-4', 'tp4-2'), ('tp4-3', 'tp5-3'),
    ('fp-3', 'tp4-3'), ('cr3-7', 'tp4-4'), ('dmg-5', 'tp4-4'), ('tp4-5', 'tp5-4'),
    # twisted path 5
    ('tp3-2', 'tp5-1'), ('cr3-2', 'tp5-2'), ('tp4-3', 'tp5-3'), ('tp4-5', 'tp5-4'),
    ('tp4-2', 'tp5-4'), ('tp2-5', 'tp5-5'),
    # crossroads 1
    ('cr1-1', 'tp2-2'), ('cr1-2', 'h?-2'), ('cr1-3', 'tp3-4'),
    ('cr1-4', 'tp3-1'), ('cr1-5', 'tp1-4'), ('cr1-5', 'tp2-5'),
    ('bt-3', 'cr1-6'), ('cr1-7', 'sb-1'),
    # crossroads 2
    ('cr2-1', 'tp1-5'), ('cr2-2', 'tp2-3'), ('cr2-3', 'fp-4'),
    ('cr2-4', 'h?-3'), ('bt-2', 'cr2-4'), ('cr2-5', 'tp2-3'),
    ('cr2-6', 'tp1-2'), ('cr2-6', 'tp3-3'), ('cr2-7', 'sb-1'),
    # crossroads 3
    ('cr3-1', 'fp-2'), ('cr3-2', 'tp5-2'), ('cr3-3', 'tp3-5'),
    ('cr3-4', 'pr-5'), ('cr3-5', 'tp2-4'), ('cr3-6', 'tp4-1'), ('cr3-7', 'tp4-4'),
]

# all edges specified alphabetically
# ensures that the embedding has vertices for the same map are close to each other
INTRA_MAP_EDGES = set([
    # haunted house
    ('hh-1', 'hh-2'),
    # bent tree
    ('bt-1', 'bt-3'), ('bt-2', 'bt-3'), ('bt-3', 'bt-4'), ('bt-3', 'bt-5'),
    # dead man's gorge
    ('dmg-1', 'dmg-2'), ('dmg-2', 'dmg-3'), ('dmg-3', 'dmg-4'),
    # swamp bog
    ('sb-1', 'sb-2'),
    # haunted ?
    ('h?-1', 'h?-2'), ('h?-2', 'h?-3'),
    # phantom road
    ('pr-1', 'pr-2'), ('pr-2', 'pr-3'), ('pr-3', 'pr-4'), ('pr-4', 'pr-5'),
    # forgotten path
    ('fp-1', 'fp-2'), ('fp-2', 'fp-3'), ('fp-3', 'fp-4'), ('fp-4', 'fp-5'),
    # twisted path
    ('tp1-1', 'tp1-2'), ('tp1-2', 'tp1-3'), ('tp1-3', 'tp1-4'), ('tp1-4', 'tp1-5'),
    ('tp2-1', 'tp2-2'), ('tp2-2', 'tp2-3'), ('tp2-3', 'tp2-4'), ('tp2-4', 'tp2-5'),
    ('tp3-1', 'tp3-2'), ('tp3-2', 'tp3-3'), ('tp3-3', 'tp3-4'), ('tp3-4', 'tp3-5'),
    # crossroads
    ('cr1-1', 'cr1-2'), ('cr1-2', 'cr1-3'), ('cr1-1', 'cr1-4'),
    ('cr1-4', 'cr1-5'), ('cr1-5', 'cr1-6'), ('cr1-6', 'cr1-7'),
    ('cr2-1', 'cr2-2'), ('cr2-2', 'cr2-3'), ('cr2-1', 'cr2-4'),
    ('cr2-4', 'cr2-5'), ('cr2-5', 'cr2-6'), ('cr2-6', 'cr2-7'),
    ('cr3-1', 'cr3-2'), ('cr3-2', 'cr3-3'), ('cr3-1', 'cr3-4'),
    ('cr3-4', 'cr3-5'), ('cr3-5', 'cr3-6'), ('cr3-6', 'cr3-7'),
])


for edge in INTER_MAP_EDGES:
    if len(edge) != 2:
        print('wrong:', edge)

for edge in INTER_MAP_EDGES:
    if edge[0] not in DETAILED_VERTICES or edge[1] not in DETAILED_VERTICES:
        print('you made a typo:', edge)
        exit()

UNIQUE_INTER_MAP_EDGES = set(INTER_MAP_EDGES)
for edge in UNIQUE_INTER_MAP_EDGES:
    if INTER_MAP_EDGES.count(edge) % 2 != 0:
        print('mismatched edge:', edge)
        exit()

for edge in INTRA_MAP_EDGES:
    if len(edge) != 2:
        print('wrong:', edge)

for edge in INTRA_MAP_EDGES:
    if edge[0] not in DETAILED_VERTICES or edge[1] not in DETAILED_VERTICES:
        print('you made a typo:', edge)
        exit()

ALL_EDGES = set.union(UNIQUE_INTER_MAP_EDGES, INTRA_MAP_EDGES)
print("Is phantom forest (detailed maps) planar?:", planarity.is_planar(list(ALL_EDGES)))

def convert_to_simplified(vertex):
    return vertex.split("-")[0]
SIMPLIFED_EDGES = set([(convert_to_simplified(v1), convert_to_simplified(v2)) for (v1, v2) in INTER_MAP_EDGES])
print("Is phantom forest (simple map) planar?:", planarity.is_planar(list(SIMPLIFED_EDGES)))
