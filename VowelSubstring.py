"""
スライディングウィンドウ

left:
開始位置:0
増加条件：rightが参照する値が母音ではないとき

right:
開始位置：k-1
増加条件：特になし / right < length of s

・ans: 時点での最適解を確保しておく(母音の数が最適解以下の場合は更新しない)
・numOfVowels: 時点での最適解の母音の数
"""


def findSubstring(s, k):
    left = 0
    right = 0
    vowels = {"a","e","i","o","u"}
    ans = "Not found!"
    currentWindow = ""
    numOfVowelsInEntire = 0
    numOfVowelsInNewWindow = 0

    # 初期ウィンドウを作成
    for right in range(k):
        if s[right] in vowels:
            numOfVowelsInEntire += 1
            numOfVowelsInNewWindow += 1
        currentWindow += s[right]
        if numOfVowelsInNewWindow != 0:
            ans = currentWindow

    for right in range(k, len(s)):
        newWindow = currentWindow

        # ウィンドウのエンドの更新
        newWindow += s[right]
        if s[right] in vowels:
            numOfVowelsInNewWindow += 1

        # ウィンドウのスタートの更新
        newWindow = newWindow[left+1:right+1]
        if s[left] in vowels:
            numOfVowelsInNewWindow -= 1
        left += 1
        
        # ウィンドウ更新に伴うデータ更新
        currentWindow = newWindow
        if numOfVowelsInNewWindow > numOfVowelsInEntire:
            numOfVowelsInEntire = numOfVowelsInNewWindow
            ans = newWindow
    print(ans)
    return ans

findSubstring("eiuaooo", 4)
# findSubstring("aeiouia", 3)