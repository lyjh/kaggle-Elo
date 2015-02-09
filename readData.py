# import pdb

def getScore():
    w_score = []
    b_score = []
    res = [] # 1: W win,-1: B win, 0: draw
    D = {'w':0, 'b':0, 'd': 0}
    for line in open('data.pgn'):
        strs = line.rstrip()[1:-1].split(' ')
        # pdb.set_trace()
        if strs[0] == 'Result':
            r = strs[1][1:-1]
            if r == '1/2-1/2':
                res.append(0)
                D['d'] += 1
            elif r == '1-0':
                res.append(1)
                D['w'] += 1
            elif r == '0-1':
                res.append(-1)
                D['b'] += 1
        elif strs[0] == 'WhiteElo':
            # pdb.set_trace()
            try:
                score = int(strs[1][1:-1])
                w_score.append(score)
            except ValueError:
                pass
        elif strs[0] == 'BlackElo':
            try:
                score = int(strs[1][1:-1])
                b_score.append(score)
            except ValueError:
                pass
        else:
            continue
    return w_score, b_score, res

def getMoveScore():
    move_score = [[0] for i in xrange(50000)]
    move_len = [1 for i in xrange(50000)]
    for line in open('stockfish.csv'):
        strs = line.rstrip().split(',')
        if strs[0] == 'Event' or not strs[1]:
            continue
        this_score = [int(s) for s in strs[1].split(' ') if s != 'NA']
        move_score[int(strs[0])-1] = this_score
        # pdb.set_trace()
        move_len[int(strs[0])-1] = len(this_score)

    return move_score, move_len

def lowerScoreWin(w_score, b_score, res):
    lw = []
    bw = []
    for i in xrange(len(w_score)):
        if w_score[i] < b_score[i] and res[i] == 1:
            lw.append(i)
        elif b_score[i] < w_score[i] and res[i] == -1:
            bw.append(i)

    return lw, bw