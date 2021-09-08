from heapq import heappop, heappush
import sys
input = sys.stdin.readline

cards = []
for _ in range(int(input())):
    heappush(cards, int(input()))

ans = 0
try:
    while cards:
        card1 = heappop(cards)
        card2 = heappop(cards) 
        ans += card1+card2
        heappush(cards, card1+card2)
except IndexError:
    print(ans)