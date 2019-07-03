#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class InsertionSort:
	def insertionSort:
		for i in range(1,n):
			j = i - 1
			if A[i] < A[j]:
				temp = A[i]
				A[i] = A[j]
				j -= 1
				while j >= 0 and A[j] > temp:
					A[j+1] = A[j]
					j -= 1
					A[j+1] = temp
		return A
