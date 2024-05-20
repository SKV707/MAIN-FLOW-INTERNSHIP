def create_list():
    n = int(input("Enter the number of elements in the list: "))
    my_list = []
    for _ in range(n):
        element = input("Enter element: ")
        my_list.append(element)
    return my_list

def list_operations(my_list):
    print("\nOriginal List:", my_list)
    
    # Add an element to the list
    element = input("Enter an element to add to the list: ")
    my_list.append(element)
    print("List after adding an element:", my_list)
    
    # Remove an element from the list
    element = input("Enter an element to remove from the list: ")
    if element in my_list:
        my_list.remove(element)
    else:
        print("Element not found in the list.")
    print("List after removing an element:", my_list)
    
    # Modify an element in the list
    index = int(input("Enter the index of the element to modify: "))
    if 0 <= index < len(my_list):
        element = input("Enter the new element: ")
        my_list[index] = element
    else:
        print("Index out of range.")
    print("List after modifying an element:", my_list)

def create_dict():
    n = int(input("\nEnter the number of key-value pairs in the dictionary: "))
    my_dict = {}
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        my_dict[key] = value
    return my_dict

def dict_operations(my_dict):
    print("\nOriginal Dictionary:", my_dict)
    
    # Add an element to the dictionary
    key = input("Enter a key to add to the dictionary: ")
    value = input("Enter a value for the key: ")
    my_dict[key] = value
    print("Dictionary after adding an element:", my_dict)
    
    # Remove an element from the dictionary
    key = input("Enter a key to remove from the dictionary: ")
    if key in my_dict:
        del my_dict[key]
    else:
        print("Key not found in the dictionary.")
    print("Dictionary after removing an element:", my_dict)
    
    # Modify an element in the dictionary
    key = input("Enter a key to modify its value: ")
    if key in my_dict:
        value = input("Enter the new value: ")
        my_dict[key] = value
    else:
        print("Key not found in the dictionary.")
    print("Dictionary after modifying an element:", my_dict)

def create_set():
    n = int(input("\nEnter the number of elements in the set: "))
    my_set = set()
    for _ in range(n):
        element = input("Enter element: ")
        my_set.add(element)
    return my_set

def set_operations(my_set):
    print("\nOriginal Set:", my_set)
    
    # Add an element to the set
    element = input("Enter an element to add to the set: ")
    my_set.add(element)
    print("Set after adding an element:", my_set)
    
    # Remove an element from the set
    element = input("Enter an element to remove from the set: ")
    if element in my_set:
        my_set.remove(element)
    else:
        print("Element not found in the set.")
    print("Set after removing an element:", my_set)
    
    # Note: Sets do not support indexing or direct modification of elements.

def main():
    print("List Operations")
    my_list = create_list()
    list_operations(my_list)
    
    print("\nDictionary Operations")
    my_dict = create_dict()
    dict_operations(my_dict)
    
    print("\nSet Operations")
    my_set = create_set()
    set_operations(my_set)

if __name__ == "__main__":
    main()
