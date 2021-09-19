function solution(people, limit) {
    //  내림차순 정렬
    people = people.sort((a, b) => b - a);
    var answer = 0;
    
    //  i = 가장 무거운 사람, j = 가장 가벼운 사람
    //  반복문 안에 두 개의 값을 선언 할 수 있는걸 처음 알았음!
    for(let i = 0, j = people.length - 1; i <= j ; i++){
        console.log(`${people[i]} + ${people[j]} = ${people[i] + people[j]}`);
        // i + j 가 limit 보다 높을 때 동숭 불가
        if(people[i] + people[j] > limit){
            answer++;
        // i + j 가 limit 보다 낮을 때 동승 가능
        // 다음으로 가벼운 사람이랑 동승 가능한지 확인
        } else {
            answer++;
            j--;
        }
    }
    return answer;
}