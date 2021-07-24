const input = Number(require('fs').readFileSync('/dev/stdin').toString());

let res = '';

for(i = input; i > 0; i--){
    res += i + '\n';
};

console.log(res);
