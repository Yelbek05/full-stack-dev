const FormElement = document.querySelector('.contact-for-submission');

FormElement.addEventListener('submit', (event) => {
    event.preventDefault();

    const formData = new FormData(FormElement);
    const data = new URLSearchParams(formData)
    fetch('https://reqres.in/api/users', {
        method: 'POST',
        // headers: {
        //     'Content-Type': 'application/x-www-form-urlencoded'
        // },
        body: data
    }).then(res => res.json())
      .then(data => {
        console.log(data);
        alert("Форма успешно отправлено!")
        FormElement.reset();
    })
      .catch(err => {
        console.log(error)
        alert("Ошибка при отправке формы. Попробуйте снова.")
      });

    // console.log({
    //     name: formData.get('fname'),
    //     email: formData.get('femail'),
    //     message: formData.get('PhoneNumber'),
    //     message: formData.get('ask-for[]')
    // });
});

// document.querySelector(".closebtn").addEventListener("click", function() {
//     document.getElementById("check").checked = false; 
// });

// function toggleMenu(){
//     let navLinks = document.querySelector(".nav-links");
//     navLinks.classList.toggle("active");
// }

  
// function handleFormSubmission(form, successMessageId, closeButtonId, webhookUrl) {
//   const submitButton = form.querySelector('button[type="submit"]');
//   const successMessage = document.getElementById(successMessageId);
//   const closeButton = document.getElementById(closeButtonId);

//   form.addEventListener('submit', async function(event) {
//       event.preventDefault();

//       const formData = new FormData(form);
//       const jsonData = {};

//       formData.forEach((value, key) => {
//           if (key.endsWith("[]")) {
//               const newKey = key.replace("[]", ""); 
//               if (!jsonData[newKey]) {
//                   jsonData[newKey] = [];
//               }
//               jsonData[newKey].push(value);
//           } else {
//               jsonData[key] = value;
//           }
//       });

//       submitButton.disabled = true;
//       submitButton.textContent = 'Отправка...';

//       try {
//           const response = await fetch(webhookUrl, {
//               method: 'POST',
//               headers: { "Content-Type": "application/json" },
//               body: JSON.stringify(jsonData)
//           });

//           if (!response.ok) throw new Error('Ошибка при отправке формы');

//           successMessage.style.display = 'block';
          
//           setTimeout(() => {
//               successMessage.style.display = 'none';
//           }, 5000);

//           form.reset();
//       } catch (error) {
//           console.error("Ошибка:", error);
//           alert("Ошибка при отправке. Попробуйте снова.");
//       } finally {
//           submitButton.disabled = false;
//           submitButton.textContent = submitButton.dataset.originalText;
//       }
//   });

//   closeButton.addEventListener('click', function() {
//       successMessage.style.display = 'none';
//   });
// }

// const form1WebhookUrl = "https://hook.eu2.make.com/g5aevehj1fmbmlz1afps61xpagxdk778";
// const bookCallWebhookUrl = "https://hook.eu2.make.com/lbtkuhblok4gt8313e4fk9l1qtpbo0q1";

// const form1 = document.getElementById('form_1');
// if (form1) {
//   const submitButton1 = form1.querySelector('button[type="submit"]');
//   submitButton1.dataset.originalText = submitButton1.textContent;
//   handleFormSubmission(form1, 'successMessage', 'closeButton', form1WebhookUrl);
// }

// const bookCallForm = document.querySelector('#bookCall .contact-for-submission');
// if (bookCallForm) {
//   const submitButton2 = bookCallForm.querySelector('button[type="submit"]');
//   submitButton2.dataset.originalText = submitButton2.textContent;
//   handleFormSubmission(bookCallForm, 'successMessage', 'closeButton', bookCallWebhookUrl);
// }


