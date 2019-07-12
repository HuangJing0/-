#!/usr/bin/env python3
#  -*- coding: UTF-8 -*-
class QuickSort:
	def q_sort(self, A, left, right):
		if left < right:
			pivot = self.partition(A, left, right)
			self.q_sort(A, left, pivot - 1)
			self.q_sort(A, pivot + 1, right)
		return A
	def partition(self, A, left, right):
		pivotkey = A[left]
		while left < right:
			while left < right and A[right] >= pivotkey:
				right -= 1
			A[left] = A[right]
			while left < right and A[left] <= pivotkey:
				left += 1
			A[right] = A[left]
		A[left] = pivotkey
		return left
	def quickSort(self, A, n):
		return self.q_sort(A, 0, n-1)
