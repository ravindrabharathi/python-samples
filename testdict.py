#group by function for dictionary

def group_by_owner(files):
    result = {}
    for key in files:
        if (files[key] in result.keys()):
            result[files[key]].append(key)
        else:
            result[files[key]] = [key]
    return result

#filenames with owners
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}




