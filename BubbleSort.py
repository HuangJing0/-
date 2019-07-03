#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class BubbleSort:
	def bubbleSort(self, A, n):
		for i in range(0,n-1):
			for j in range(0, n-1-j):
				if A[i] > A[i+1]:
					A[i],A[i+1] = A[i+1],A[i]
		return A
