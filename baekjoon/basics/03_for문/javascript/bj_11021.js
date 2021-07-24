let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

for (let a = 1; a <= input[0]; a++) {
  let number = input[a].split(" ");

  console.log(`Case #${a}: ${Number(number[0]) + Number(number[1])}`);
}