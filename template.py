# 複数の配列を取得(事前に要素が未定義の場合)
import sys

nums = []
for line in sys.stdin:
    nums.append(int(line.strip()))

# 複数の配列を取得(空白区切り)
list(map(int, input().split()))

# 最初の行で行数nを取得し、次のn行を処理
n = int(input())
lines = [input() for _ in range(n)]