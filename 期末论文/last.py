Private Sub Command1_Click()
Dim q As Single, r As Single, m As Single, i As Single, k As Single
Dim x As Single, y As Single, vx As Single, vy As Single, h As Single
Dim ax As Double, ay As Double, aax As Double, aay As Double
Dim n As Single, t As Single, rr As Single, mm As Single
Dim vvx As Single, vvy As Single

Scale (-6.5 * 10 ^ -13, 5 * 10 ^ -13)-(6.5 * 10 ^ -13, -4.5 * 10 ^ -13)
Line (-6 * 10 ^ -13, 4 * 10 ^ -13)-(6 * 10 ^ -13, -4 * 10 ^ -13), , B
For i = -10 To 10
Line (-6 * 10 ^ -13, i * 4 * 10 ^ -13 / 10)-(-5.9 * 10 ^ -13, i * 4 * 10 ^ -13 / 10)
Line (5.9 * 10 ^ -13, i * 4 * 10 ^ -13 / 10)-(6 * 10 ^ -13, i * 4 * 10 ^ -13 / 10)
Line (i * 6 * 10 ^ -13 / 10, -4 * 10 ^ -13)-(i * 6 * 10 ^ -13 / 10, -3.9 * 10 ^ -13)
Line (i * 6 * 10 ^ -13 / 10, 4 * 10 ^ -13)-(i * 6 * 10 ^ -13 / 10, 3.9 * 10 ^ -13)
Next i
q = 79 * 1.6 * 10 ^ -19
r = 7.5 * 10 ^ -14
m = 6.64 * 10 ^ -27 '粒子重量
mm = 197 * 1.66 * 10 ^ -27 '金核重量
e = 1.6 * 10 ^ -19
k = 8.99 * 10 ^ 9
h = 10 ^ -22
vx = 2 * 10 ^ 7   '粒子速度
vy = 0
xx = 2 * 10 ^ -13 '金核位置
yy = 0
n = 2 * k * q * e / m
If r >= 80 * 10 ^ -14 Then r = 80 * 10 ^ -14
Circle (xx, 0), r, vbRed
rr = Sqr((x - 2 * 10 ^ -13) ^ 2 + (y - 0) ^ 2)
ax = n * (x - 2 * 10 ^ -13) / rr ^ 3     '粒子初始加速度
ay = n * (y - 0) / rr ^ 3
vx = vx + h * ax / 2                     '粒子初始速度
vy = vy + h * ay / 2
For t = -1 * 10 ^ -13 To 1 * 10 ^ -13 Step 0.05 * 10 ^ -13
vx = 2 * 10 ^ 7
vy = 0
y = t
For x = -6 * 10 ^ -13 To 6 * 10 ^ -13 Step 0.001 * 10 ^ -13
rr = Sqr((x - 2 * 10 ^ -13) ^ 2 + (y - 0) ^ 2)
ax = n * (x - 2 * 10 ^ -13) / rr ^ 3
ay = n * (y - 0) / rr ^ 3
If y <= -4 * 10 ^ -13 Then Exit For
If y >= 4 * 10 ^ -13 Then Exit For
If x < -6 * 10 ^ -13 Then Exit For
PSet (x, y)
If rr >= r Then
ax = n * (x - 2 * 10 ^ -13) / rr ^ 3
ay = n * (y - 0) / rr ^ 3
End If
If rr < r Then
ax = n * (x - 2 * 10 ^ -13) / r ^ 3
ay = n * (y - 0) / r ^ 3
End If
vx = vx + h * ax
vy = vy + h * ay
x = x + h * vx
y = y + h * vy
Next x
Next t
End Su