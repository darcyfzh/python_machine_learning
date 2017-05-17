'''
@Author: Darcy
@Date: May, 17, 2017
@Topic: SBS
A classic sequential feature selection algorithm is Sequential Backward Selection (SBS)
which aims to reduce the dimensionality of the initial feature subspace 
with a minimum decay in performance of the classifier 
to improve upon computational efficiency
'''
from sklearn.base import clone
from itertools import combinations
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

class SBS:
	def __init__(self, estimator, k_features,scoring=accuracy_score,
		         test_size=0.25, random_state=1):
		self.scoring = scoring
		self.estimator = clone(estimator)
		self.k_features = k_features
		self.test_size = test_size
		self.random_state = random_state

	def fit(self, X, Y):
		x_train, y_train, x_test, y_test = \
				train_test_split(X, Y, test_size = self.test_size, 
									random_state = self.random_state) 
		dim = np.shape(x_train)[1]
		self.indices = tuple(range(dim))
		self.subSets_ = [self.indices]
		score = self.calScore(self.x_train, y_train, x_test, y_test, self.indices)
		self.scores_ = [score]
		while dim > self.k_features:
			scores = []
			subSet = []
			for p in combinations(self.indices, dim - 1):
				score = self.calScore(self.x_train, y_train, x_test, y_test, p)
				scores.append(score)
				subSet.append(p)
			best = np.argmax(score)
			self.indices = subSet[best]
			self.subSets_.append(self.indices)
			dim -= 1
			self.scores_.append(scores[best])
		self.k_score = self.scores_[-1]
		return self


	def calScore(self, x_train, y_train, x_test, y_test, indices):
		self.estimator.fit(x_train, y_train)
		y_pred = self.estimator.predict(x_test)
		score = self.scoring(y_test, y_pred)
		return score


