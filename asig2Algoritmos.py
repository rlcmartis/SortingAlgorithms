#!/usr/bin/python

#==================================================#
#                                                  #
#  Developers: Ramón Collazo & Luis Albertorio     #
#  Course: Analysis of Algorithms                  #
#  Professor: Edusmildo Orozco                     #
#  Homework #2                                     #
#                         M                        #
#                      <~/|\~>                     #
#                                                  #
#  Implementation in python language of the known  #
#  algorithms of sorting: Insertion, Heap, Quick   #
#  and Merge Sorting.                              #
#                                                  #
#==================================================#

from sys import exit
import math
import random

# Helper function for some of the algorithms
# It swaps two elements of an Array by their indices
def swap(A, i, j):
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp

#~~~~~~~~~~~~~~~~~~INSERTION-SORT~~~~~~~~~~~~~~~~~~~~
# Implementation for the insertion sort algorithm
def insertionSort(A):
	# We are gonna go through subarrays of the
	# original array that has the elements from
	# 0 to i, being those i+1 elements the same
	# of A but in sorted order
	for i in range(1, len(A)):
		# In insertion sort a new element is 
		# added to a sorted subarray, so we compare
		# that element with the sorted ones (from highest 
		# to lowest), while those elements are greater
		# than the new one we keep moving it to the left
		# untill we find an element equal or less than 
		# it. We that happens the subarray is sorted in
		# ascending order.
		j = i # Index of the new element
		unsorted = True # We start assuming is unsorted
		# Loop to sort the subarray
		while unsorted:
			# If the one of the left is not greater than
			# the new element, then the subarray is
			# sorted
			if (j==0) or (A[j] >= A[j-1]):
				unsorted = False
			else:
				# If the element on the left is greater
				# than our new element, then we switch 
				# positions
				swap(A, j, j-1)
				j-=1 # The index of the element changed

#~~~~~~~~~~~~~~~~~~~~HEAP-SORT~~~~~~~~~~~~~~~~~~~~~~~
# Implementation for the heap sort algorithm
def heapSort(A):
	# Max_Heapify the tree
	heapified = False
	while not heapified:
		heapified = maxHeapify(A)

	# Now that the three is heapified
	for k in range(len(A),2,-1):
		swap(A,0,k-1)
		heapifyFromRoot(A,k-1)

# Two helper functions to calculate child's indices.
# (Also helps the code to be easy-to-read)
def left(i):
	return (2*(i+1))-1
def right(i):
	return (2*(i+1))

# Do to the array a Max Heap for binary threes
def maxHeapify(A):
	# We start heapifying from the last parent to the root
	j = int(math.floor(len(A)/2))-1 #index of last parent

	# Flag to know if going through all the parents
	# no changes were made (this means the binary tree 
	# is completely heapified)
	noChanges = True
	for i in range(j, -1, -1): # (from j downto 0)
		l = left(i)
		r = right(i)

		# Look the greatest between parent and child(s)
		# and swap if needed
		if r >= len(A): #has one left child
			if A[l] < A[i]:
				swap(A,i,l)
				noChanges = False
		else: #has the two childs
			if (A[l] > A[i]) or (A[r] > A[i]):
				if A[l] > A[r]:
					swap(A,i,l)
				else:
					swap(A,i,r)
				noChanges = False

	return noChanges

def heapifyFromRoot(A,k):
	i = 0
	while i<k:
		l = left(i)
		r = right(i)
		if l >= k: #has no childs
			break
		elif r >= k: #has one left child
			if A[l] < A[i]:
				swap(A,i,l)
				i = l-1
		else: #has the two childs
			if (A[l] > A[i]) or (A[r] > A[i]):
				if A[l] > A[r]:
					swap(A,i,l)
					i = l-1
				else:
					swap(A,i,r)
					i = r-1
		i+=1

#~~~~~~~~~~~~~~~~~~~~QUICK-SORT~~~~~~~~~~~~~~~~~~~~~~
# Implementation for the quick sort algorithm
def quicksort(A, lo, hi):
	if(lo < hi):
		print "---> %s" % (A)
		p = partition(A, lo, hi)
		quicksort(A, lo, p - 1)
		quicksort(A, p + 1, hi)

	return A

def partition(A, lo, hi):
	# set pivot
	pivot = A[lo]
	left = lo+1
	right = hi
	done = False
	# we reorder element in the list so everything below the pivot comes
	# before and anything higher comer after it
	while not done:
		while left <= right and A[left] <= pivot:
			left = left + 1
		while A[right] >= pivot and right >= left:
			right = right - 1
		if right < left:
			done = True
		else:
			swap(A, left, right)
	swap(A, lo, right)
	return right


#~~~~~~~~~~~~~~~~~~~~MERGE-SORT~~~~~~~~~~~~~~~~~~~~~~
# Implementation for the merge sort algorithm
def mergeSort(A):
	if len(A) <= 1:
		return A
	# left and right list
	left=[]
	right=[]
	# find the middle of the list
	mid = len(A)/2
	
	#left side of the list
	left = A[:mid]
	
	#right side of the list
	right = A[mid:]

	print "left: %s" % (left)
	print "right: %s" % (right)
	
	# call the function recursively so that the left and
	# right list keep being cut down the middle till there's
	# only one element left in the list
	mergeSort(left)
	mergeSort(right)

	# merge function to merge all elements
	return merge(A, left, right)
	
# function that merges all elements
def merge(A, left, right):
	# counters
	i=j=k=0
	
	while i<len(left) and j<len(right):
		#if the left element on the list is lower replace it in the original list and up counter
		if left[i] < right[j]:
			A[k] = left[i]
			i=i+1
		else:
		#else right is lower
			A[k] = right[j]
			j=j+1
		k=k+1

	#if right list is over then dum left list
	while i<len(left):
		A[k] = left[i]
		i=i+1
		k=k+1
	#if left list is over then dump right
	while j < len(right):
		A[k] = right[j] 
		j=j+1
		k=k+1

	return A

#~~~~~~~~~~~~~~~~~~~~~~~~~Main Program~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print "Enter one of the numbers of the following sort algorithms: "
print "1) Insertion Sort"
print "2) Heap Sort"
print "3) Quick Sort"
print "4) Merge Sort"
option = raw_input("Option: ")
try:
	option = int(option)
except:
	print "Error! Cannot recognize your option. It must be from 1-4."
	exit(1)

print "Now it's time to create an array."
comma = raw_input("Enter the comma separated elements of A=")
strings = comma.split(",")
A = []
for element in strings:
	try:
		A.append(int(element))
	except:
		print "Elements for A must be intergers (ex:'2,1,6') Exiting...\n"
		exit(1)

if option==1:
	insertionSort(A)
elif option==2:
	heapSort(A)
elif option==3:
	A = quicksort(A, 0, len(A)-1)
else:
	A = mergeSort(A)

print A