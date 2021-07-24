const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();

let n = Number(input);
let sum = 0;

for(i = 0; i < n; i++){
    sum = sum + (i+1);
}

console.log(sum);