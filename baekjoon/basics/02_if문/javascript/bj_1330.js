const fs = require('fs');
const a = Number(fs.readFileSync('/dev/stdin').toString());

if(a >= 90) {
    console.log('A')
} else if(a < 90 && a >= 80) {
    console.log('B')
} else if(a < 80 && a >= 70) {
    console.log('C')
} else if(a < 70 && a >= 60) {
    console.log('D')
} else {
    console.log('F')
}