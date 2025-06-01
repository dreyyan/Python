def topFrequentElement(arr, k):
    elements = {}
    
    for i in arr:
        if i not in elements:
            elements[i] = 1
        else:
            elements[i] += 1
            
    for i in range(k + 1):
        
    for key, value in elements.items():
        print(f"{key}: {value} times")
            
        
topFrequentElement([1, 1, 1, 2, 3], 2)