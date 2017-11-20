from collections import Counter

def most_frequent(data):
    c = Counter(data)
    list = c.keys()
    
    return list


x = most_frequent(['a', 'a', 'bi', 'bi', 'bi'])
print(x)
'''y = max(x.values())
print(y)
'''
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
'''
