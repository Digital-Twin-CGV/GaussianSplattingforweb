import numpy as np

def solve_linear_equations(x1, y1, gauss_x1, gauss_z1, x2, y2, gauss_x2, gauss_z2):
    # 미니맵 X, Y 좌표와 가우시안 X, Z 좌표를 이용한 선형 방정식 풀기
    
    # X 좌표에 대한 방정식: gauss_x = A * x + B
    A, B = np.linalg.solve([[x1, 1], [x2, 1]], [gauss_x1, gauss_x2])
    
    # Z 좌표에 대한 방정식: gauss_z = C * y + D
    C, D = np.linalg.solve([[y1, 1], [y2, 1]], [gauss_z1, gauss_z2])
    
    return A, B, C, D

# 예시 데이터
x1, y1 = 10.21982280210603, 68.51576957342863
gauss_x1, gauss_z1 = 2.7809713456745833, 581.6324058711705

x2, y2 = 9.231135277725695, 49.94388015551212
gauss_x2, gauss_z2 = -37.16518410492816, -292.1577651300937

# 계수 계산
A, B, C, D = solve_linear_equations(x1, y1, gauss_x1, gauss_z1, x2, y2, gauss_x2, gauss_z2)

# 결과 출력
print(f"gauss_x = {A:.3f} * xPixel + {B:.3f}")
print(f"gauss_z = {C:.3f} * yPixel + {D:.3f}")
