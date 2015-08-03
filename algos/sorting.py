# Implimentation of various sorting algorithms for our_lists
##########################

def swappa_list(our_list, low, high):
    our_list[low], our_list[high] = our_list[high], our_list[low]
    print(our_list)
    return our_list


def selection_sort(our_list):
    """
    Look through the our_list.  Find the smallest element.  Swap it to the front.
    Repeat.
    """

    for start in range(len(our_list)):
        min_index = start
        smallest = our_list[start]
        # find smallest num
        # enumerate DOES NOT WORK
        for key in range(start + 1, len(our_list)):
            if our_list[key] < smallest:
                print("I am smaller", our_list[key], "than", smallest)
                min_index = key
                smallest = our_list[key]
        if min_index != start:
            swappa_list(our_list, start, min_index)
    return our_list

def insertion_sort(our_list):
    """ 
    Insert (via swaps) the next element in the sorted our_list of the previous
    elements.
    """
    for start in range(len(our_list) + 1, len(our_list)):
        offset = start - 1
        if our_list[start] <  our_list[start - 1]:
            swappa_list(our_list, start, offset)

def merge_sort(our_list):
    """
    Our first recursive algorithm.
    """
    pass
