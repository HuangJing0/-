#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
class MergeSort:
	def merge(self, a, b):
		M = []
		i = j = 0
		while i<len(a) and j<len(b):
			if a[i] < b[j]:
				M.append(a[i])
				i += 1
			else:
				M.append(b[j])
				j += 1
		if i == len(a):
			for l in b[j:]:
				M.append(l)
		else:
			for l in a[i:]:
				M.append(l)
		return(M)

	def mergeSort(self, A, n):
		n = len(A)
		if n <= 1:
			return A
		mid = n//2
		a = self.mergeSort(A[:mid], n)
		b = self.mergeSort(A[mid:], n)
		return self.merge(a,b)
