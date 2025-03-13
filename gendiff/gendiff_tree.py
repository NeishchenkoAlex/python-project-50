

def build_tree(data1, data2):
    result = []
    all_keys = sorted(set(data1) | set(data2))
    for key in all_keys:
        item1 = data1.get(key)
        item2 = data2.get(key)
        if isinstance(item1, dict) and isinstance(item2, dict):
            result.append({'key': key, 'type': 'nested', 
                           'children': build_tree(item1, item2)})
        elif key in data1 and key in data2:
            if item1 != item2:
                result.append({'key': key, 'type': 'changed', 
                               'old_value': item1, 'new_value': item2})
            else:
                result.append({'key': key, 'type': 'unchanged', 'value': item1})
        elif key in data1 and key not in data2:
            result.append({'key': key, 'type': 'deleted', 'value': item1})
        elif key not in data1 and key in data2:
            result.append({'key': key, 'type': 'added', 'value': item2})

    return result



    
    

