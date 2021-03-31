"""
    AtCoder Heuristic Contest 001
    解答
    by　koncha
"""

"""
    拡張可能かどうかを確かめる

    Parameters
    ----------
    upper_left : (int, int)
        長方形の左上の座標
    lower_right : (int, int)
        長方形の右下の座標

    Return
    ----------
    can_extend : bool
        他の広告と被らずに拡張可能か
"""
def can_extend(upper_left, lower_right):
    global ans
    global now

    if not in_space(upper_left, lower_right):
        return False

    for i, x in enumerate(ans):
        if now == i:
            continue
        if x[2] <= upper_left[0] or x[0] >= lower_right[0] or x[1] >= lower_right[1] or x[3] <= upper_left[1]:
            continue
        return False
    return True

"""
    長方形の面積を求める

    Parameters
    ----------
    upper_left : (int, int)
        長方形の左上の座標
    lower_right : (int, int)
        長方形の右下の座標

    Return
    ----------
    S : int
        長方形の面積
"""
def now_S(upper_left, lower_right):
    return (lower_right[0] - upper_left[0]) * (lower_right[1] - upper_left[1])

"""
    外枠からはみ出しているかどうかを確かめる

    Parameters
    ----------
    upper_left : (int, int)
        長方形の左上の座標
    lower_right : (int, int)
        長方形の右下の座標

    Return
    ----------
    is_in_space : bool
        広告表示領域に入っているかどうか
"""
def in_space(upper_left, lower_right):
    global W
    return bool(not tuple(filter(lambda x: not(0 <= x <= W), upper_left + lower_right)))
"""
    特定の方向に拡張する

    Parameters
    ----------
    course : str
        拡張する方向を定義
    upper_left : (int, int)
        長方形の左上の座標
    lower_right : (int, int)
        長方形の右下の座標

    Return
    ----------
    upper_left : (int, int)
        長方形の左上の座標
    lower_right : (int, int)
        長方形の右下の座標
"""
def extend(course, upper_left, lower_right, S):
    global up
    if course == "l":
        next_upper_left, next_lower_right = [upper_left[0] - up, upper_left[1]], lower_right
    elif course == "r":
        next_upper_left, next_lower_right = upper_left, [lower_right[0] + up, lower_right[1]]
    elif course == "d":
        next_upper_left, next_lower_right = upper_left, [lower_right[0], lower_right[1] + up]
    elif course == "u":
        next_upper_left, next_lower_right = [upper_left[0], upper_left[1] - up], lower_right

    if can_extend(next_upper_left, next_lower_right) and now_S(next_upper_left, next_lower_right) <= S:
        return next_upper_left, next_lower_right
    else:
        return upper_left, lower_right

"""
    時間計測用のタイマーを定義
"""
class Timer:
    """
        コンストラクタ
    """
    def __init__(self):
        import time
        self.time = time

    """
        タイマーを開始する
        開始した時刻が0となる
    """
    def timer_start(self):
        self.start = self.time.time()

    """
        経過時間がオーバーしているかどうかを確認する

        Parameters
        ----------
        ms : int
            目標経過時刻

        Return
        ----------
        is_over : bool
            時間を超えていたらTrue、超えていなければFalse
    """
    def is_over(self, ms):
        return (self.time.time() - self.start > ms/1000)

"""
    解答を出力する
"""
def print_ans():
    global ans
    for a in ans:
        print(" ".join(map(str, a[:-1])))

def last_extend():
    global ans
    global W

    for i, item in enumerate(ans):
        if item[4] <= now_S(item[0:2], item[2:4]):
            continue
        small = 0
        big = W
        for j, a in enumerate(ans):
            if i == j:
                continue
            if a[0] >= item[2] or a[2] <= item[0]:
                continue
            if a[1] >= item[3]:
                big = min(a[1], big)
            else:
                small = max(a[3], small)

        if small < ans[i][1]:
            if now_S([ans[i][0], small], ans[i][2:4]) <= item[4]:
                ans[i][1] = small
        if big > ans[i][3]:
            if now_S(ans[i][0:2], [ans[i][2], big]) <= item[4]:
                ans[i][3] = big

        small = 0
        big = W
        for j, a in enumerate(ans):
            if i == j:
                continue
            if a[1] >= item[3] or a[3] <= item[1]:
                continue
            if a[0] >= item[2]:
                big = min(a[0], big)
            else:
                small = max(a[2], small)

        if small < ans[i][0]:
            if now_S([small, ans[i][1]], ans[i][2:4]) <= item[4]:
                ans[i][0] = small
        if big > ans[i][2]:
            if now_S(ans[i][0:2], [big, ans[i][3]]) <= item[4]:
                ans[i][2] = big


import random

n = int(input())
data = []
W = 10000
up = 1
ans = []
timer = Timer()
course = 0
courses = ["l", "r", "u", "d"]

for _ in range(n):
    data.append(list(map(int, input().split())))

"""
    初期の解答を作成する
"""
for a in data:
    ans.append([a[0], a[1], a[0]+1, a[1]+1, a[2]])

timer.timer_start()
while not timer.is_over(4300):
    now = random.randint(0, n-1)
    ans[now][0:2], ans[now][2:4] = extend(courses[course], ans[now][0:2], ans[now][2:4], ans[now][-1])
    course += 1
    course %= 4

# last_extend()
print_ans()
