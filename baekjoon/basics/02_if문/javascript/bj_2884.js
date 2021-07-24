const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');

let x = Number(input[0]);
let y = Number(input[1]);

y -= 45

if(y < 0){
  y += 60
  x--

  if(x === -1){
    x = 23
  }
}

console.log(x + ' ' + y)