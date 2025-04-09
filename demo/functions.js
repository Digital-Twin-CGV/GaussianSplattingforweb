// 로봇 마커 생성 함수
function createRobotMarker(robot, minimapRectClass) {
  // 미니맵의 정보
  const minimapRect = document
    .getElementById(minimapRectClass)
    .getBoundingClientRect();
  // marker 넣을 container
  const container = document.createElement("div");
  container.className = "robot_marker_container";
  container.style.position = "absolute";
  container.style.left =
    ((robot.position[0] + 2750) * 100) / 3299 -
    (12 * 100) / minimapRect.width +
    "%";
  container.style.top =
    ((-robot.position[1] + 2457) * 100) / 3133 -
    (35 * 100) / minimapRect.height +
    "%";
  container.style.display = "flex";
  container.style.alignItems = "flex-start";
  container.style.cursor = "pointer";

  // marker
  const marker = document.createElement("div");
  marker.className = "robot_marker";
  marker.innerHTML = `${robot.id}`;
  marker.style.setProperty("--marker-color", applyColor(robot)); //css에 값 넘기기

  container.appendChild(marker);

  container.addEventListener("click", () => {
    updateTitle(robot.id, robot.status);
  });

  return container;
}

// marker, label 색상 지정
function applyColor(robot) {
  if (robot.status === 1) {
    // 사용중이라면?
    return "#ff0000";
  } else if (robot.battery < 30) {
    // 배터리가 30 이하라면?
    return "#f2d406";
  } else {
    // 나머지
    return "#1dd200";
  }
}
