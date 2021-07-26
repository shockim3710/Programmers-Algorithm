a, b = map(int, input().strip().split(' '))
# a만큼 *의 개수를 추가하여 b만큼 반복
for i in range(b):
    print('*' * a)