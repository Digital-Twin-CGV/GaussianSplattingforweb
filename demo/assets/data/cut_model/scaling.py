# import numpy as np

# def solve_linear_equations(x1, y1, gauss_x1, gauss_z1, x2, y2, gauss_x2, gauss_z2):
#     # 미니맵 X, Y 좌표와 가우시안 X, Z 좌표를 이용한 선형 방정식 풀기
    
#     # X 좌표에 대한 방정식: gauss_x = A * x + B
#     A, B = np.linalg.solve([[x1, 1], [x2, 1]], [gauss_x1, gauss_x2])
    
#     # Z 좌표에 대한 방정식: gauss_z = C * y + D
#     C, D = np.linalg.solve([[y1, 1], [y2, 1]], [gauss_z1, gauss_z2])
    
#     return A, B, C, D

# # 예시 데이터
# x1, y1 = 15.658492016300958, 13.2062793964938
# gauss_x1, gauss_z1 = 2780.6669889832947, -2558.5591961901564

# x2, y2 = 19.55679955911998, 28.55048561480667
# gauss_x2, gauss_z2 = 2608.8405149246732, -1879.9950359554957

# A, B, C, D = solve_linear_equations(x1, y1, gauss_x1, gauss_z1, x2, y2, gauss_x2, gauss_z2)

# # 결과 출력
# print(f"gaussianX = {A:.3f} * x + {B:.3f}")
# print(f"gaussianZ = {C:.3f} * y + {D:.3f}")


import numpy as np

def solve_linear_equations_least_squares(x_list, y_list, gauss_x_list, gauss_z_list):
    # x -> gauss_x 매핑 (A, B 추정)
    X_matrix = np.vstack([x_list, np.ones(len(x_list))]).T
    A, B = np.linalg.lstsq(X_matrix, gauss_x_list, rcond=None)[0]
    
    # y -> gauss_z 매핑 (C, D 추정)
    Y_matrix = np.vstack([y_list, np.ones(len(y_list))]).T
    C, D = np.linalg.lstsq(Y_matrix, gauss_z_list, rcond=None)[0]
    
    return A, B, C, D

# 예시 데이터 (4개 점)
x_list = [ 87.41258741258741 , 90.62937062937063  , 83.4965034965035 ,87.27272727272727  ]
y_list =  [ 80.85233679269163 , 86.15412936926157  ,88.06866557746739  , 85.27049727316658 ]
gauss_x_list = [ -153.71235695917144, -301.6421028188169, -13.640710304461997, -135.59745337164307]
gauss_z_list = [ 121.80720095101596, 317.12044994038195, 365.9321607150147, 241.7433180417521]
#[ , , , ]
A, B, C, D = solve_linear_equations_least_squares(x_list, y_list, gauss_x_list, gauss_z_list)

# 결과 출력
print(f"gaussianX = {A:.3f} * x + {B:.3f}")
print(f"gaussianZ = {C:.3f} * y + {D:.3f}")

