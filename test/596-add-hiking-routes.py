# https://www.openstreetmap.org/way/12188550
# https://www.openstreetmap.org/relation/2684235
assert_has_feature(
    12, 654, 1582, 'roads',
    { 'kind': 'path', 'highway': 'track' })

# https://www.openstreetmap.org/way/109993139
# NOTE: part of *cycle* network, not walking network.
#assert_has_feature(
#    12, 655, 1586, 'roads',
#    { 'kind': 'path', 'highway': 'cycleway' })

# https://www.openstreetmap.org/way/25292070
assert_has_feature(
    14, 2620, 6334, 'roads',
    { 'kind': 'path', 'highway': 'steps', 'name': 'Esmeralda Ave.' })

# https://www.openstreetmap.org/way/346093021
assert_has_feature(
    15, 5235, 12671, 'roads',
    { 'kind': 'path', 'highway': 'footway' })

# http://www.openstreetmap.org/way/344205837
assert_has_feature(
    15, 5234, 12667, 'roads',
    { 'kind': 'path', 'highway': 'footway' })

# http://www.openstreetmap.org/way/5260896
# http://www.openstreetmap.org/relation/3718820
# Baker River Road - residential - part of Pacific Northwest Trail (nwn)
# should be visible at z11
assert_has_feature(
    11, 331, 706, 'roads',
    { 'kind': 'minor_road', 'highway': 'residential', 'walking_network': 'nwn' })

# http://www.openstreetmap.org/way/5254587
# http://www.openstreetmap.org/relation/3718820
# Mount Baker Highway - secondary - part of Pacific Northwest Trail (nwn)
# should be visible at z11
assert_has_feature(
    11, 331, 704, 'roads',
    { 'kind': 'major_road', 'highway': 'secondary',
      'walking_network': 'nwn' })

# http://www.openstreetmap.org/way/5857215
# http://www.openstreetmap.org/relation/3718820
# Whiskey Bend Road - unclassified - part of Pacific Northwest Trail (nwn)
# should be visible at z11
assert_has_feature(
    11, 320, 712, 'roads',
    { 'kind': 'minor_road', 'highway': 'unclassified',
      'walking_network': 'nwn' })

# http://www.openstreetmap.org/way/6671321
# http://www.openstreetmap.org/relation/2381423
# Matz Road - service - part of Ice Age National Scenic Trail (nwn)
# should be visible at z11
assert_has_feature(
    11, 514, 751, 'roads',
    { 'kind': 'minor_road', 'highway': 'service', 'walking_network': 'nwn' })

# http://www.openstreetmap.org/way/16000421
# http://www.openstreetmap.org/relation/1544944
# Dogbane - service=driveway - part of American Discovery Trail (nwn)
# should be visible at z11
assert_has_feature(
    11, 491, 762, 'roads',
    { 'kind': 'minor_road', 'highway': 'service', 'service': 'driveway',
      'walking_network': 'nwn' })
