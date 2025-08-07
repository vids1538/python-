h2={"name":"vidya sagar","class": "bca","roll":21875,"mobile":7461905442}

keys = list(h2.keys())  # Get all keys of the dictionary

i = 0
while i < len(keys):
    key = keys[i]
    print(key, ":", h2[key])
    i += 1
