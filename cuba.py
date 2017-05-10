label = {
    ('Hambalang', 'Andi'): 1,
    ('Andi', 'Hambalang'): 3,
    ('Hambalang', 'Wafid Muharram'): 2,
    ('Andi', 'Andi Malarangeng'): 1,
    ('Andi Malarangeng', 'Wafid Muharram'): 1,
    ('Wafid Muharram', 'Andi'): 1
}

graph = [
    ('Hambalang', 'Andi'), ('Andi', 'Hambalang'), ('Hambalang', 'Wafid Muharram'), ('Andi', 'Andi Malarangeng'),
    ('Andi Malarangeng', 'Wafid Muharram'), ('Wafid Muharram', 'Andi')
]

temp = {}

for item in label:
    if label[item] > 1:
        print item
        temp[item] = label[item]

print temp