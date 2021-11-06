N = int(input())
pikes = []
for i in range(N):
    pikes.append(int(input().split()[1]))

M = int(input())
traces = []
for i in range(M):
    traces.append(list(map(int, input().split())))


def find_elevation_right(pikes):
    elevation = [0] * len(pikes)
    for i in range(1, len(pikes)):
        if pikes[i] - pikes[i-1] > 0:
            elevation[i] = pikes[i] - pikes[i-1]
    return elevation

def find_elevation_left(pikes):
    elevation = [0] * len(pikes)
    for i in range(1, len(pikes)):
        if pikes[i-1] - pikes[i] > 0:
            elevation[i] = pikes[i-1] - pikes[i]
    return elevation


def find_prefix_sum(elevation):
    prefix_sum = [0] * (len(elevation) + 1)
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i-1] + elevation[i-1]
    return prefix_sum


def find_traces_elevation(pikes, traces):
    chain_elevation_right = find_prefix_sum(find_elevation_right(pikes))
    chain_elevation_left = find_prefix_sum(find_elevation_left(pikes))
    traces_elevation = []
    for i in range(len(traces)):
        trace = traces[i]
        if trace[1] > trace[0]:
            elevation = chain_elevation_right[trace[1]] - chain_elevation_right[trace[0]]
            traces_elevation.append(elevation)
        else:
            elevation = chain_elevation_left[trace[0]] - chain_elevation_left[trace[1]]
            traces_elevation.append(elevation)
    return traces_elevation


for elevation in find_traces_elevation(pikes, traces):
    print(elevation)