const input = Number(require('fs').readFileSync('/dev/stdin').toString());
let res = '';

for(i = 1; i <= input; i++) {
    res += '*'.repeat(i) + '\n'
}
console.log(res);