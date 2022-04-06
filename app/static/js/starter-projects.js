async function post(url, data) {
    const response = await fetch(url, {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    const payload = await response.json()
    return payload
}

async function applyFormSubmitAction(e) {
    e.preventDefault();
    const name = e.target.name.value
        .toLowerCase()
        .normalize('NFKD')
        .replace(/[^\w]/g, '')
    const starterProjectId = e.target.number.value;

    if (!name) {
        alert("You must enter your name before starting the exercise !");
        return;
    }
    const responseUser = await post("/api/users/", { name })
    console.log(responseUser)
    const responseProject = await post(`/api/users/${responseUser.user.id}/projects/`, { starterProjectId })
    console.log(responseProject)
    window.location.pathname = `/users/${responseUser.user.id}/projects/${responseProject.project.id}`;
}

async function setStarterProjects() {
    const response = await fetch('/api/starter-projects')
    const data = await response.json()
    const htmlForm = document.getElementById('starter-projects')
    console.log(data)
    htmlForm.innerHTML = data.starter_projects.map(p => `<option value="${p.id}">${p.name.replace("_", " ") }</option>`)
}

function main() {
    setStarterProjects()
    document.querySelector("form").addEventListener("submit", applyFormSubmitAction);
}

main()
