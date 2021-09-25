function solution(priorities, location) {
    
    let answer = 0
    let indexList = []
    for (let i = 0 ; i < priorities.length ; i++) {
        indexList.push(i)
    }
    
    let max = Math.max(...priorities)
    
    while(true){
        let index = indexList.shift();
        if(priorities[index] < max) {
            indexList.push(index)
        } else {
            answer++
            priorities[index] = 0;
            max = Math.max(...priorities)
            if (index === location) {
                return answer
            }
        }
        
    }

}