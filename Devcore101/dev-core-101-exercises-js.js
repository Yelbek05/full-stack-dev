// 1. **Конвертация температуры**
//     - Напиши программу, которая принимает температуру в Цельсиях и переводит её в Фаренгейты.
// 2. **Чётное или нечётное**
//     - Напиши программу, которая принимает число от пользователя и выводит, чётное оно или нечётное.
// 4. **Игра "Угадай число"**
//     - Напиши программу, которая генерирует случайное число и позволяет пользователю его угадать, сообщая, больше или меньше загаданное число.

// №1

// function celciusToFarenhit(celcius){
//     return (celcius * 1.8) + 32;
// }
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });
// rl.question("Enter in Celsius: ", (input)=>{
//     let celcius = parseFloat(input);
//     let fahrenheit = celciusToFarenhit(celcius);
//     console.log(`${celcius} C is equal to ${fahrenheit}`);

//     rl.close();
// });


// №2

// function isEven(num){
//     if(num % 2 === 0){
//         return "Even";
//     }
//     else{
//         return "Odd";
//     }
// }
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });
// rl.question("Number: ", (input) =>{
//     let number = parseInt(input, 10);
//     console.log(isEven(number));
//     rl.close();
// });

// №4

// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// const randomNum = Math.floor(Math.random() * 100) + 1;

// function isEqual(){
//     rl.question("Number: ", (input) =>{
//         let num = parseInt(input, 10);
//         if(num > randomNum){
//             console.log("Too Much");
//             isEqual();
//         }
//         else if(num < randomNum){
//             console.log("Too Little");
//             isEqual();
//         }
//         else{
//             console.log("Ta tadaam, You guessed it, YOU WON!!!");
//             rl.close();
//         }
//     });
// }
// console.log("let's guess the number");
// isEqual();






