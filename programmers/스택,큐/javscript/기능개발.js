function solution(progresses, speeds) {
    var answer = [];
    let daysLeft = [];
    
    for(let i = 0; i < progresses.length; i++){
        let progLeft = 100 - progresses[i];
        let dayLeft = Math.ceil(progLeft / speeds[i])
        daysLeft.push(dayLeft);
    }
    
    while (daysLeft.length != 0) {
        let j = daysLeft.shift();
        let count = 1;
        while (j >= daysLeft[0]){
            count++;
            daysLeft.shift();
        }
        answer.push(count)
    }
    return answer;
}