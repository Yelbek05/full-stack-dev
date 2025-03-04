const contactForm = document.getElementById('contactForm');

contactForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const name = contactForm.name.value.trim();
    const email = contactForm.email.value.trim();
    const message = contactForm.message.value.trim();
    
    if (name && email && message) {
        contactForm.style.display = 'block';
        contactForm.style.color = 'red';
        contactForm.innerHTML = 'Form is sent successfully';
        
        contactForm.reset();
    }

    if (name && email && message){
        console.log("Имя: ", name);
        console.log("Email: ", email);
        console.log("Сообщение: ", message);
    }
    
    else {
        contactForm.style.display = 'block';
        contactForm.style.color = 'green';
        contactForm.innerText = 'please fill all fields';
    }
});
