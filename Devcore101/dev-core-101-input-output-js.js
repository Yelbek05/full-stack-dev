//For a browser:
// let n = prompt("Name: ");
// let a = prompt("Age: ");
// let b = 100 - a;
// console.log(`You have left ${b} years to get 100 years old`);

//In node.js
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
readline.question('Name: ', name=>{
    readline.question('Age: ', age=>{
        let b = 100 - parseInt(age, 10);
        console.log(`You have left ${b} years to get 100 years old`);
        readline.close();
    });
});
