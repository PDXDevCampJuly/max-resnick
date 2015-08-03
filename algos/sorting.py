# Implimentation of various sorting algorithms for our_lists
##########################

def swappa_list(our_list, low, high):
    our_list[low], our_list[high] = our_list[high], our_list[low]
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
    for start in range(1, len(our_list)):
        candidate = our_list[start]
        candidate_index = start - 1
        while candidate_index >= 0:
            print(candidate_index)
            print(candidate, our_list[candidate_index])
            if candidate < our_list[candidate_index]:
                swappa_list(our_list, candidate_index, candidate_index + 1)
                candidate_index -= 1
            else:
                break
    return our_list

def merge_sort(our_list):
    """
    Our first recursive algorithm.
    """
    pass


some_list = [5, 4, 3, 2]