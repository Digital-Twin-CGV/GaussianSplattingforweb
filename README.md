
# Garo: Web-based Robot Monitoring System using Gaussian Splatting 
## 가우시안 스플래팅을 활용한 웹 기반 로봇 관제 시스템 제작

**2025 Spring Capstone Design Project**  
**2025 봄학기 캡스톤디자인 2** <br>
**Advisor:** Prof. Hwang Sungsoo 황성수 교수님 <br>
**Partner Company:** SensingPlus 센싱플러스 <br>
**Team:** 심성환, 김유겸, 김예지, 김예빈 

---

## Overview 개요

최근 자율주행 기술의 발전으로 실시간으로 원격으로 로봇을 관제할 수 있는 시스템의 수요가 증가하고 있다.   

기존 시스템은 대부분 2D 기반으로 구성되어 있어 공간 이해도가 낮는 사람이 사용하게 되었을때 어려움을 겪을 수 있고, 원하는 목적지를 정밀하게 선택하기 어렵다는 문제점을 가지고 있다. 

본 프로젝트는 **Gaussian Splatting 기반의 3D 디지털 트윈 환경** 을 웹상에 구현하여 로봇의 위치, 경로, 상태 정보를 **실시간으로 시각화하고 제어할 수 있는 관제 시스템(Garo)** 을 설계하였다.

---

## Motivation 프로젝트 동기

기존의 2D 로봇 관제 인터페이스는 공간 인식이 제한적이며,  
로봇이 실제 공간에서 어디에 위치해있는지 직관적으로 파악하기 어렵다.  
Gaussian Splatting은 이미지로부터 고품질의 3D 장면을 빠르게 재구성할 수 있는 기술로, 별도의 LiDAR 없이도 현실과 유사한 3D 환경을 만들 수 있다는 점에서 최적의 대안이었다.  

이를 통해 **저비용·고현실감의 로봇 관제 시각화 플랫폼**을 구축하고자 했다.

---

## Objectives  목표

- Gaussian Splatting을 활용해 실제 공간에 대응되는 3D 모델 생성  
- 로봇의 위치 데이터를 실시간으로 반영하는 웹 기반 관제 UI 구현  
- 사용자 인터랙션 기반의 로봇 이동 명령 및 상태 모니터링 기능 제공  
- Node.js + Supabase 기반 실시간 데이터 연동 및 동기화  

---

## Key Features  주요 기능

- **3D 공간 시각화:** COLMAP으로 생성한 sparse point cloud를 Gaussian Splatting 모델로 변환  
- **실시간 로봇 위치 갱신:** 로봇의 좌표 데이터를 수신하여 웹페이지에 실시간 반영  
- **웹 기반 제어 인터페이스:** 사용자가 브라우저 상에서 로봇의 경로를 설정 및 이동명령  
- **데이터베이스 동기화:** Supabase를 활용한 사용자-로봇 간 양방향 데이터 처리  

---

## Tech Stack  기술 스택

| Category | Technologies |
|-----------|---------------|
| 3D Reconstruction | COLMAP, Gaussian Splatting |
| Rendering | Three.js, Supersplat |
| Backend | Node.js |
| Database | Supabase |
| Development | GitHub |

---

## Implementation Details  세부 구현 설명

- **학습 이미지 변환 스크립트 작성**: 가우시안 스플래팅 모델의 일관성을 위해 학습에 필요한 이미지 후처리 작업 자동화 스크립트 작성 
- **데이터베이스 기반 실시간 통신**: 로봇 좌표를 실시간 스트림으로 수신 및 브라우저 반영  
- **Three.js 최적화**: Gaussian 모델의 해상도 및 렌더링 부하를 조절하기 위한 분할 업로드  
- **UI 구조화**: 로봇 목록, 3D Model 뷰, 실시간 상태창으로 구성된 UI 설계  
- **미니맵과 3d model 좌표 매핑** : 2D 미니맵에서 클릭한 위치에 해당하는 3D 모델로 이동하는 좌표 매핑 계산식 제작

---

## System Architecture  시스템 구조 (파이프라인)

<img height="100" src="https://github.com/Digital-Twin-CGV/GaussianSplattingforweb/blob/main/images/systemArchitecture.png">

---

## Technical Challenges & Solutions  기술적 문제와 해결방법

| Challenge | Solution |
|------------|-----------|
| Gaussian Splatting 모델 좌표계와 2D 로봇 미니맵 좌표 불일치 | 1차 방정식을 활용한 좌표 매핑 계산식 활용 |
| Gaussian Splatting 모델의 렌더링 지연 | 분할 업로드 |
| Gaussian Splatting 모델의 인터랙션 문제 | 건물의 바닥, 천장에 해당하는 부분을 메쉬로 만들어 해결 |

---

## Deployment & Demo  실행 및 데모 영상

- **Live Demo:** https://gaussian-splattingforweb.vercel.app/  
- **Demo Video:** [YouTube Link](https://youtu.be/G8lRnJHhhe4?si=AD9zh3tn8FmVEQwz)  
- **Repository:** [GitHub Repository](https://github.com/Digital-Twin-CGV/GaussianSplattingforweb#)

---

## What We Learned  배운점

- Gaussian Splatting의 구조와 WebGL 렌더링 최적화 방법 이해  
- 3D Reconstruction과 Web Frontend 간의 데이터 파이프라인 설계 경험  
- 로봇 제어, 시각화, 데이터베이스 관리의 통합적 시스템 설계 역량 강화  

---

## Future Work  추후 개선사항

- 로봇 이동 예상 경로 표시  
- 3D 모델의 퀄리티 향상
- Unity 기반 인터페이스 확장 및 안정성 확보
- Supabase 관리자 인증 시스템 및 사용자 대시보드 강화
 

---

## Team Roles  팀역할

| Name | Role | Responsibilities |
|------|------|------------------|
| **심성환** | Team Leader / Backend Developer | Node.js 서버 및 Supabase 데이터 구조 설계 |
| **김유겸** | Backend Developer | 웹 사용자 인터랙션 구현, 2D 지도와 3D 모델간의 좌표 매핑 |
| **김예지** | Frontend Developer | 웹페이지 UI 구현, Three.js 기반 상호작용 구현 |
| **김예빈** | Integration Engineer | COLMAP 및 Gaussian Splatting 변환 작업, 2D 지도와 3D 모델간의 좌표 매핑 |

---
