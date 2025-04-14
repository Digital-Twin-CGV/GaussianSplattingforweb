import numpy as np

def solve_linear_equations(x1, y1, gauss_x1, gauss_z1, x2, y2, gauss_x2, gauss_z2):
    # 미니맵 X, Y 좌표와 가우시안 X, Z 좌표를 이용한 선형 방정식 풀기
    
    # X 좌표에 대한 방정식: gauss_x = A * x + B
    A, B = np.linalg.solve([[x1, 1], [x2, 1]], [gauss_x1, gauss_x2])
    
    # Z 좌표에 대한 방정식: gauss_z = C * y + D
    C, D = np.linalg.solve([[y1, 1], [y2, 1]], [gauss_z1, gauss_z2])
    
    return A, B, C, D

# 예시 데이터
x1, y1 = 15.658492016300958, 13.2062793964938
gauss_x1, gauss_z1 = 2780.6669889832947, -2558.5591961901564

x2, y2 = 19.55679955911998, 28.55048561480667
gauss_x2, gauss_z2 = 2608.8405149246732, -1879.9950359554957

A, B, C, D = solve_linear_equations(x1, y1, gauss_x1, gauss_z1, x2, y2, gauss_x2, gauss_z2)

# 결과 출력
print(f"gaussianX = {A:.3f} * x + {B:.3f}")
print(f"gaussianZ = {C:.3f} * y + {D:.3f}")
