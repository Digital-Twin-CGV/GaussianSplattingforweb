
# Garo: Web-based Robot Monitoring System using Gaussian Splatting 
## 가우시안 스플래팅을 활용한 웹 기반 로봇 관제 시스템 제작

**2025 Spring Capstone Design Project**  
**2025 봄학기 캡스톤디자인 2** <br>
**Advisor:** Prof. Hwang Sungsoo 황성수 교수님 <br>
**Partner Company:** SensingPlus 센싱플러스 <br>
**Team:** 심성환, 김유겸, 김예지, 김예빈 

---

## 📌 Overview  

최근 자율주행 기술의 발전으로 실시간으로 원격으로 로봇을 관제할 수 있는 시스템의 수요가 증가하고 있다.   

기존 시스템은 대부분 2D 기반으로 구성되어 있어 공간 이해도가 낮는 사람이 사용하게 되었을때 어려움을 겪을 수 있고, 원하는 목적지를 정밀하게 선택하기 어렵다는 문제점을 가지고 있다. 

본 프로젝트는 **Gaussian Splatting 기반의 3D 디지털 트윈 환경** 을 웹상에 구현하여 로봇의 위치, 경로, 상태 정보를 **실시간으로 시각화하고 제어할 수 있는 관제 시스템(Garo)** 을 설계하였다.

---

## 💡 Motivation  

기존의 2D 로봇 관제 인터페이스는 공간 인식이 제한적이며,  
로봇이 실제 공간에서 어디에 위치해있는지 직관적으로 파악하기 어렵다.  
Gaussian Splatting은 이미지로부터 고품질의 3D 장면을 빠르게 재구성할 수 있는 기술로, 별도의 LiDAR 없이도 현실과 유사한 3D 환경을 만들 수 있다는 점에서 최적의 대안이었다.  

이를 통해 **저비용·고현실감의 로봇 관제 시각화 플랫폼**을 구축하고자 했다.

---

## 🎯 Objectives  

- Gaussian Splatting을 활용해 실제 공간에 대응되는 3D 모델 생성  
- 로봇의 위치 데이터를 실시간으로 반영하는 웹 기반 관제 UI 구현  
- 사용자 인터랙션 기반의 로봇 이동 명령 및 상태 모니터링 기능 제공  
- Node.js + Supabase 기반 실시간 데이터 연동 및 동기화  

---

## 🔑 Key Features  

- **3D 공간 시각화:** COLMAP으로 생성한 sparse point cloud를 Gaussian Splatting 모델로 변환  
- **실시간 로봇 위치 갱신:** 로봇의 좌표 데이터를 수신하여 웹페이지에 실시간 반영  
- **웹 기반 제어 인터페이스:** 사용자가 브라우저 상에서 로봇의 경로를 설정 및 이동명령  
- **데이터베이스 동기화:** Supabase를 활용한 사용자-로봇 간 양방향 데이터 처리  

---

## 🧩 Tech Stack  

| Category | Technologies |
|-----------|---------------|
| 3D Reconstruction | COLMAP, Gaussian Splatting |
| Rendering | Three.js, Supersplat |
| Backend | Node.js |
| Database | Supabase |
| Development | GitHub |

---

## 🛠 Implementation Details  

- **COLMAP 자동화 파이프라인 구축**: 업로드된 이미지 세트를 기반으로 camera pose와 point cloud 생성  
- **Gaussian 변환 스크립트 작성**: COLMAP 결과를 Gaussian Splatting 형식으로 자동 변환  
- **WebSocket 기반 실시간 통신**: 로봇 좌표를 실시간 스트림으로 수신 및 브라우저 반영  
- **Three.js 최적화**: Gaussian 모델의 해상도 및 렌더링 부하를 조절하기 위한 LOD(Level of Detail) 적용  
- **UI 구조화**: 로봇 목록, 카메라 뷰, 실시간 상태창으로 구성된 React-like SPA 설계  

---

## 🧱 System Architecture  

<a href="https://www.inria.fr/"><img height="100" src="assets/logo_inria.png"> </a>

---

## 🧩 Technical Challenges & Solutions  

| Challenge | Solution |
|------------|-----------|
| Gaussian Splatting 모델 좌표계와 로봇 좌표 불일치 | COLMAP camera pose 행렬을 변환하여 월드 좌표계 통합 |
| Supersplat 모델의 렌더링 지연 | LOD(Level of Detail) 적용 및 프레임 버퍼 동적 업데이트 |
| 실시간 데이터 동기화 지연 | WebSocket 기반 비동기 스트리밍 및 서버 캐싱 개선 |
| Gaussian 모델 대용량 문제 | Gaussian 수집 시 threshold 기반 filtering 적용 |

---

## 🚀 Deployment & Demo  

- **Live Demo:** https://gaussian-splattingforweb.vercel.app/  
- **Demo Video:** [YouTube Link](https://youtu.be/G8lRnJHhhe4?si=AD9zh3tn8FmVEQwz)  
- **Repository:** [GitHub Repository](https://github.com/Digital-Twin-CGV/GaussianSplattingforweb#)

---

## 🎓 What We Learned  

- Gaussian Splatting의 구조와 WebGL 렌더링 최적화 방법 이해  
- 3D Reconstruction과 Web Frontend 간의 데이터 파이프라인 설계 경험  
- 로봇 제어, 시각화, 데이터베이스 관리의 통합적 시스템 설계 역량 강화  

---

## 📈 Future Work  

- 로봇 이동 예상 경로 표시  
- 3D 모델의 퀄리티 향상
- Unity 기반 인터페이스 확장 및 안정성 확보
- Supabase 관리자 인증 시스템 및 사용자 대시보드 강화
 

---

## 👥 Team Roles  

| Name | Role | Responsibilities |
|------|------|------------------|
| **심성환** | Team Leader / Backend Developer | Node.js 서버 및 Supabase 데이터 구조 설계 |
| **김유겸** | Backend Developer | 웹 사용자 인터랙션 구현, 2D 지도와 3D 모델간의 좌표 매핑 |
| **김예지** | Frontend Developer | 웹페이지 UI 구현, Three.js 기반 상호작용 구현 |
| **김예빈** | Integration Engineer | COLMAP 및 Gaussian Splatting 변환 작업, 2D 지도와 3D 모델간의 좌표 매핑 |

---
