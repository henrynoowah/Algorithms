class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        int pos;
        for(int i = 0; i < seoul.length; i++){
            if(seoul[i].equals("Kim")){
                answer = "김서방은 " +i+ "에 있다";
                break;
            }
        }
        return answer;
    }
}