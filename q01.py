import pkg.modu as m

print('請輸入三角形的 3 個頂點坐標')
print('-' * 30)
vertex1 = map(int, input('請輸入頂點 a 的坐標：').split(','))
vertex2 = map(int, input('請輸入頂點 b 的坐標：').split(','))
vertex3 = map(int, input('請輸入頂點 c 的坐標：').split(','))
print('-' * 30)
output = m.triangle_zhonxin(tuple(vertex1), tuple(vertex2), tuple(vertex3))
print(f"此三角形的重心為：{output}")
