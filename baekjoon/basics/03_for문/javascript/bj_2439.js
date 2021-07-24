const input = Number(require('fs').readFileSync('/dev/stdin').toString());
let res = '';

for(i = 1; i <= input; i++) {
    res += ' '.repeat(input - i) + '*'.repeat(i) + '\n'
}
console.log(res);