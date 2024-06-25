def merge_dictionaries(dict1, dict2):
    larger = dict1 if len(dict1) > len(dict2) else dict2
    smaller = dict1 if len(dict1) < len(dict2) else dict2
    for key in smaller:
        larger[key] = smaller[key]
    return larger


contacts1 = {
    "David": "123",
    "Carter": "456",
    "Molly": "789",
    "John": "234",
}
contacts2 = {
    "David": "+012",
    "Harry": "+234",
}
print("merged ->", {**contacts1, **contacts2})
