def handScore(a):
    nums = []
    for x in xrange(0, len(a)):
        nums.append(a[x][0])
    for x in xrange(0, len(nums)):
        if nums[x] == 'T':
            nums[x] = 10
        elif nums[x] == 'J':
            nums[x] = 11
        elif nums[x] == 'Q':
            nums[x] = 12
        elif nums[x] == 'K':
            nums[x] = 13
        elif nums[x] == 'A':
            nums[x] = 14
        nums[x] = int(nums[x])
    nums = sorted(nums)
    suits = []
    for x in xrange(0, len(a)):
        suits.append(a[x][1])
    # Royal flush
    if int(nums[4]) == 14 and int(nums[3]) == 13 and int(nums[2]) == 12 and int(nums[1]) == 11 and int(nums[0]) == 10 and (a[0][1] == a[1][1] == a[2][1] == a[3][1] == a[4][1]):
        return 10

    # stright flush
    if int(nums[4]) == int(nums[0]) + 4 and int(nums[3]) == int(nums[0]) + 3 and int(nums[2]) == int(nums[0]) + 2 and int(nums[1]) == int(nums[0]) + 1 and (a[0][1] == a[1][1] == a[2][1] == a[3][1] == a[4][1]):
        return [9, nums[0]]

    # 4 of a kind
    for x in xrange(0, len(nums)):
        check = nums[x]
        if nums.count(check) == 4:
            return [8, nums[x]]

    # full house
    three = False
    two = False
    card = 0
    for x in xrange(0, len(nums)):
        check = nums[x]
        if nums.count(check) == 3:
            three = True
            card = nums[x]
        elif nums.count(check) == 2:
            two = True
    if three and two:
        return [7, nums[x]]

    # flush
    if suits.count(suits[0]) == 5:
        return [6, max(nums)]

    # straight
    if int(nums[4]) == int(nums[0]) + 4 and int(nums[3]) == int(nums[0]) + 3 and int(nums[2]) == int(nums[0]) + 2 and int(nums[1]) == int(nums[0]) + 1:
        return [5, nums[0]]

    # 3 of a kind
    for x in xrange(0, len(nums)):
        check = nums[x]
        if nums.count(check) == 3:
            return [4, nums[x]]

    # 2 pair
    pair1 = False
    pair2 = False
    previousCheck = 0
    pair1Card = 0
    pair2Card = 0
    for x in xrange(0, len(nums)):
        check = nums[x]
        if nums.count(check) == 2:
            pair1 = True
            previousCheck = nums[x]
            pair1Card = nums[x]
    for y in xrange(0, len(nums)):
        check = nums[y]
        if nums.count(check) == 2 and check != previousCheck:
            pair2 = True
            pair2Card = nums[y]
    if pair1 and pair2:
        return [3, max(pair1Card, pair2Card)]

    # pair
    for x in xrange(0, len(nums)):
        check = nums[x]
        if nums.count(check) == 2:
            return [2, nums[x]]

    # high card
    return [1, max(nums)]


f = open("poker.txt", 'r')
string = f.read()
a = string.split("\n")
counter = 0
for x in xrange(0, len(a)):
    a[x] = a[x].split(" ")
a = a[:-1]
for x in xrange(0, len(a)):
    player1 = []
    player2 = []
    for i in xrange(0, 5):
        player1.append(a[x][i])
        player2.append(a[x][i + 5])
    p1Score = handScore(player1)
    p2Score = handScore(player2)
    if p1Score[0] > p2Score[0]:
        counter += 1
    elif p1Score[0] == p2Score[0]:
        if p1Score[1] > p2Score[1]:
            counter += 1
print counter
