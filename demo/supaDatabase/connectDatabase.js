const supabaseUrl = 'https://ocfxzzwdonwyyolcomii.supabase.co';
const supabaseKey =
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9jZnh6endkb253eXlvbGNvbWlpI' +
  'iwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzc1MTk3NzgsImV4cCI6MjA1MzA5NTc3OH0.9CvzDp5t5Atn7UU9dJqXRaps6SrtMWBZQnKW3FnEA1Y';
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

  console.log(password);

  return password.password;
}

getPassword();

export default supabase;
export { getPassword };
