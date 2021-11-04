N = int(input())
pikes = []
for i in range(N):
    pikes.append(int(input().split()[1]))

M = int(input())
traces = []
for i in range(M):
    traces.append(list(map(int, input().split())))


def findelevationright(pikes):
    elevation = [0] * len(pikes)
    for i in range(1, len(pikes)):
        if pikes[i] - pikes[i-1] > 0:
            elevation[i] = pikes[i] - pikes[i-1]
    return elevation

def findelevationleft(pikes):
    elevation = [0] * len(pikes)
    for i in range(1, len(pikes)):
        if pikes[i-1] - pikes[i] > 0:
            elevation[i] = pikes[i-1] - pikes[i]
    return elevation


def findprefixsum(elevation):
    prefixsum = [0] * (len(elevation) + 1)
    for i in range(1, len(prefixsum)):
        prefixsum[i] = prefixsum[i-1] + elevation[i-1]
    return prefixsum


def findtraceselevation(pikes, traces):
    chain_elevation_right = findprefixsum(findelevationright(pikes))
    chain_elevation_left = findprefixsum(findelevationleft(pikes))
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


for elevation in findtraceselevation(pikes, traces):
    print(elevation)