const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();

let n = Number(input);
let res = '';

for(i = 0; i < n; i++) {
    res += i+1 + '\n';
}

console.log(res)