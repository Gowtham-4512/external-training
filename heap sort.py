def heap_sort(arr):
    n = len(arr)

    # Build a max-heap from the array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Swap the root of the heap with the last element
        arr[i], arr[0] = arr[0], arr[i]

        # Restore the max-heap property for the remaining heap
        heapify(arr, i, 0)

def heapify(arr, n, i):
    """
    Heapify a subtree rooted with node i which is an index in arr[].
    n is size of heap
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)
