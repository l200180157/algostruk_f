from modul5_Kegiatan import *

A = [1,2,3,7,8,9]
B = [4,5,6,10,11,12]

def gabungUrut(list1, list2):
    C = list1 + list2
    insertionSort(C)
    return C
