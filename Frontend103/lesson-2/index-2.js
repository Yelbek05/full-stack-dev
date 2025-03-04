const products = [
    {name: "Apple", price: 1.99},
    {name: "Banana", price: 60.78},
    {name: "Orange", price: 2.99}
];

const user = {
    name:"Yelbek",
    age: 20,
    purchases: ["apple", "banana"]
}
// Updating...:
user.email = "Marlanbayev@gmail.com";
user.age = 15;
user.purchases = ["orange", "Kakao"]

// delete user.purchases

console.log("User details: ", Object.entries(user));

const filterProducts = products.filter(product => product.price > 40);
console.log(filterProducts);

//in loop:
for (let key in user){
    console.log(key, user[key])
}
// output:
// abstract@Lenovo:~/full-stack-dev-new/Frontend103/lesson-2$ node ./index-2.js
// [ { name: 'Banana', price: 60.78 } ]

products.forEach((product, index) => {
    console.log(product, index);
});

const increasrPrice = products.map(product => {
    return {
        ...product,
        price: product.price * 2
    }
})
console.log(increasrPrice);
// output:
// [
//     { name: 'Apple', price: 3.98 },
//     { name: 'Banana', price: 121.56 },
//     { name: 'Orange', price: 5.98 }
// ]

const object = {
    message: "Hello Mr.Dog double G ",
    init: function() {
        const showMessage = () => {
            console.log(this.message);
        };
    showMessage();
    }
};

object.init();
