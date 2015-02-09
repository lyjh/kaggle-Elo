from readData import *
import numpy as np
from sklearn import linear_model

train_N = 25000

w_score, b_score, res = getScore()
move_score, move_len = getMoveScore()

b_mean = np.mean(b_score)
w_mean = np.mean(w_score)
move_score_mean = [np.mean(m) for m in move_score]

X_train = res[:train_N]
X_train = np.vstack((X_train, move_score_mean[:train_N]))
X_train = np.vstack((X_train, move_len[:train_N]))

X_test = res[train_N:]
X_test = np.vstack((X_test, move_score_mean[train_N:]))
X_test = np.vstack((X_test, move_len[train_N:]))

X_b_train = [b_mean for i in xrange(train_N)]
X_w_train = [w_mean for i in xrange(train_N)]

X_b_test = np.vstack((X_b_train, X_test))
X_w_test = np.vstack((X_w_train, X_test))

X_b_train = np.vstack((X_b_train, X_train))
X_w_train = np.vstack((X_w_train, X_train))

w_score = np.array(w_score)
b_score = np.array(b_score)

X_b_train = np.transpose(X_b_train)
X_w_train = np.transpose(X_w_train)
X_b_test = np.transpose(X_b_test)
X_w_test = np.transpose(X_w_test)

bfit = linear_model.LinearRegression()
wfit = linear_model.LinearRegression()

bfit.fit(X_b_train, b_score)
wfit.fit(X_w_train, w_score)

b_pred = bfit.predict(X_b_test)
w_pred = wfit.predict(X_w_test)

file = open('submission.csv', 'w')
file.write('Event,WhiteElo,BlackElo\n')
for i in xrange(25001, 50001):
    file.write('%s,%.3f,%.3f\n' % (i, w_pred[i-25001], b_pred[i-25001]))
file.close()