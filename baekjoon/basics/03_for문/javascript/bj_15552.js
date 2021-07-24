let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let answer = ''
let no = Number(input[0]);

for (i = 1; i <= no; i++) {
    let num = input[i].split(' ');
    answer += Number(num[0]) + Number(num[1]) + '\n';
}

console.log(answer);