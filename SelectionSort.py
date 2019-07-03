#!/usr/bin/env python3
 -*- coding: UTF-8 -*-
class SelectionSort:
	def selectionSort(self, A, n):
		for i in range(0, n-1):
			for j in range(i+1, n):
				if A[j] < A[i]:
					temp = A[j]
					A[j] = A[i]
					A[i] = temp
		return A
