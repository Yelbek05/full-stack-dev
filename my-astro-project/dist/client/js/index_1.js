document.querySelector(".closebtn").addEventListener("click", function() {
  document.getElementById("check").checked = false; 
});

function handleFormSubmission(form, successMessageId, closeButtonId, webhookUrl) {
  const submitButton = form.querySelector('button[type="submit"]');
  const successMessage = document.getElementById(successMessageId);
  const closeButton = document.getElementById(closeButtonId);

  form.addEventListener('submit', async function(event) {
      event.preventDefault(); // Prevent page redirect

      const formData = new FormData(form);
      const jsonData = {}; // Convert FormData to JSON object

      formData.forEach((value, key) => {
          if (key.endsWith("[]")) {
              // Handle multiple values for checkboxes
              const newKey = key.replace("[]", ""); 
              if (!jsonData[newKey]) {
                  jsonData[newKey] = [];
              }
              jsonData[newKey].push(value);
          } else {
              jsonData[key] = value;
          }
      });

      // Disable submit button to prevent multiple submissions
      submitButton.disabled = true;
      submitButton.textContent = 'Отправка...';

      try {
          const response = await fetch(webhookUrl, {
              method: 'POST',
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(jsonData)
          });

          if (!response.ok) throw new Error('Ошибка при отправке формы');

          // ✅ Show success message
          successMessage.style.display = 'block';
          
          // ⏳ Hide the success message after 5 seconds
          setTimeout(() => {
              successMessage.style.display = 'none';
          }, 5000);

          // 🔄 Clear the form
          form.reset();

      } catch (error) {
          console.error("Ошибка:", error);
          alert("Ошибка при отправке. Попробуйте снова.");
      } finally {
          // 🔄 Re-enable the submit button
          submitButton.disabled = false;
          submitButton.textContent = submitButton.dataset.originalText;
      }
  });

  // ❌ Close success message when the close button is clicked
  closeButton.addEventListener('click', function() {
      successMessage.style.display = 'none';
  });
}

// ✅ Webhook URLs from Make (Replace with actual URLs)
const form1WebhookUrl = "https://hook.eu2.make.com/g5aevehj1fmbmlz1afps61xpagxdk778";
const bookCallWebhookUrl = "https://hook.eu2.make.com/lbtkuhblok4gt8313e4fk9l1qtpbo0q1";

// ✅ Handle form_1
const form1 = document.getElementById('form_1');
if (form1) {
  const submitButton1 = form1.querySelector('button[type="submit"]');
  submitButton1.dataset.originalText = submitButton1.textContent;
  handleFormSubmission(form1, 'successMessage', 'closeButton', form1WebhookUrl);
}

// ✅ Handle bookCall form (Fix applied)
const bookCallForm = document.querySelector('#bookCall .contact-for-submission');
if (bookCallForm) {
  const submitButton2 = bookCallForm.querySelector('button[type="submit"]');
  submitButton2.dataset.originalText = submitButton2.textContent;
  handleFormSubmission(bookCallForm, 'successMessage', 'closeButton', bookCallWebhookUrl);
}
