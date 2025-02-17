const supabaseUrl = 'https://mehftlxjzwhcwtfdkffs.supabase.co';
const supabaseKey =
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1laGZ0bHhqendoY3d0ZmRrZmZzIiwic' +
  'm9sZSI6ImFub24iLCJpYXQiOjE3Mzg3Mzk2MDYsImV4cCI6MjA1NDMxNTYwNn0.bhkGt85MTdWgfuPjma8DjIXF8mXFSuXVHcSLNmtB-sQ';
const client = supabase.createClient(supabaseUrl, supabaseKey);

async function getPassword() {
  // 관리자 페이지 암호 가져오기
  let { data: password, error } = await client
    .from('password')
    .select('password')
    .single();

  if (error) {
    console.error('Error fetching password:', error);
    return null;
  }

  return password;
}

async function getRobots() {
  // 로봇 정보 가져오기
  const { data, error } = await client.from('robots').select('*');

  if (error) {
    console.error('Error fetching data:', error);
  }

  return data;
}

async function insertRequest(robotId, drive, goalPosition) {
  // request 테이블에 데이터 추가
  const { data, error } = await client
    .from('request')
    .insert([{ robot_id: robotId, drive: drive, goal_position: goalPosition }])
    .select();
  console.log(data);
  if (error) {
    console.error('Error insert data:', error);
  }

  return data;
}

async function getRequest() {
  const { data, error } = await client.from('request').select('*');

  if (error) {
    console.error('Error fetching data:', error);
  }

  return data;
}

export default supabase;
export { getPassword, getRobots, getRequest, insertRequest, client };
