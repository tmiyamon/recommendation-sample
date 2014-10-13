# -*- coding: utf-8 -*-

from math import sqrt;

def print_mat(mat):
    for line in mat:
        print line

def calc_pearson(data):
    user_count = len(data)

    ave = [sum(d, 0.0) / len(d) for d in data]

    result = []

    for x in xrange(user_count):
        user_similarities = []

        for y in xrange(user_count):
            ab = 0
            a_sq = 0
            b_sq = 0

            for i in xrange(user_count):

                a_part = data[x][i] - ave[x]
                b_part = data[y][i] - ave[y]

                ab   += a_part * b_part
                a_sq += pow(a_part, 2)
                b_sq += pow(b_part, 2)

            r_ab = ab / ( sqrt(a_sq) * sqrt(b_sq) )

            user_similarities.append(r_ab)
        result.append(user_similarities)

    return result


data = [[2,-1,0,1,-1,0],
       [-1,-1,-1,2,1,0],
       [2,0,2,1,-1,-1],
       [0,0,0,-1,1,1]]

print '## Data ##'
print_mat(data)
print ''

similarities = calc_pearson(data)

print '## Similarity ##'
print_mat(similarities)
print ''

for i, user_similatiries in enumerate(similarities):
    print 'User:', i
    most_simiarity, similar_user_index = sorted(zip(user_similatiries, range(len(user_similatiries))), reverse=True)[1]
    print '  The most similar user is', similar_user_index, 'with similarity', most_simiarity

    recommended = []
    for degree, product_index in sorted(zip(data[similar_user_index], range(len(data[similar_user_index]))), reverse=True):
        if degree > 0 and degree > data[i][product_index]:
            recommended.append(product_index)
    print '  Redommended:', recommended

