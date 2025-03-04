const addProjectButton = document.getElementById('addProject');
const projectsContainer = document.getElementById('projectsContainer');
const deleteAllProject = document.getElementById('deleteAllProject');
let counter = 0;

addProjectButton.addEventListener('click', () => {
    counter++;

    const projectCard = document.createElement('div');

    projectCard.className = 'project-card';
    projectCard.innerHTML = `
        <h2>Project ${counter}</h2>
        <p>Project description${counter}</p>
        <button class="delete-project">Delete</button>`;

    projectsContainer.appendChild(projectCard);

    // const deleteButton = projectCard.querySelector('.delete-project');
    // deleteButton.addEventListener('click', () => {
    //     projectCard.remove();
    // });
    // instead to delete can be used below:
    projectsContainer.addEventListener("click", (event) => {
        if (event.target.classList.contains("delete-project")) {
            event.target.parentElement.remove();
        }    
    });

    projectsContainer.addEventListener("click", (event) => {
        if (projectCard.children.length === 0){
            const emptyMessage = document.createElement('p');
            emptyMessage.id = 'emptyMessage';
            emptyMessage.innerText = "No projects added yet, press the button to add";
            projectsContainer.appendChild(emptyMessage);
        }

        if (document.getElementById("emptyMessage")){
            document.getElementById("emptyMessage").remove();
        }
    });
    deleteAllProject.addEventListener("click", () => {
        projectsContainer.innerHTML = '';
    })
});