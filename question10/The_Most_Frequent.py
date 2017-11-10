from collections import Counter

def most_frequent(data):
    c = Counter(data)
    return c



x = most_frequent(['a', 'a', 'bi', 'bi', 'bi'])
y = max(x.values())


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
