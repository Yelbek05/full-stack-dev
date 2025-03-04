const aboutText = document.getElementById('aboutText');
const updateButton = document.getElementById('updateAbout');

updateButton.addEventListener('click', () => {
    aboutText.innerHTML = 'This is an updated text';
});

const AboutHeading = document.getElementById('aboutHeading');
AboutHeading.style.color = 'green';
AboutHeading.style.fontSize = '50px';
AboutHeading.style.fontWeight = 'bold';

const button = document.querySelector('#updateAbout');
button.innerText = 'Update About';