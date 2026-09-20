def file(name):
    with open(name, 'r') as f:
        return f.read().strip().splitlines()
    
file('input.txt')    
