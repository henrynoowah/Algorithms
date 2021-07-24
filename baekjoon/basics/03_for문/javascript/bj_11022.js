const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

for(i = 1; i <= input[0]; i++){
    let a = input[i].split(' ');
    console.log(`Case #${i}: ${Number(a[0])} + ${Number(a[1])} = ${Number(a[0]) + Number(a[1])}`)
}
