numberOfMembers = int(input())
members = []


class Members:
    secondName = ''
    points = 0
for i in range(numberOfMembers):
    properties = list(input().split())
    m = Member()
    m.secondName = properties[0]
    m.points = int(properties[1])
    members.append(p)
members.sort(key=lambda part: -part.points)
for m in members:
    print(m.secondName)
