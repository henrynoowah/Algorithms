const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let res = '';

let n = Number(input[0].split(' ')[0]);
let x = Number(input[0].split(' ')[1]);

let num = input[1].split(' ');

for(i = 0; i < n; i++){
    if(Number(num[i])<x){
        res += num[i] + ' ';
    }
}
console.log(res)