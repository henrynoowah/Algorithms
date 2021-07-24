let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

for (i = 1; i < input.length -1; i++) {
    let numbers = input[i].split(' ');
    
    console.log(Number(numbers[0]) + Number(numbers[1]));
}