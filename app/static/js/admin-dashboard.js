let studentCodeUrl = ''
const codeAreaElement = document.getElementById("code-viewer")
codeAreaElement.value = ""

async function displayStudentFileContent() {
    if (studentCodeUrl){
        const request = await fetch(studentCodeUrl)
        if (request.status === 200) {
            const data = await request.json()
            codeAreaElement.value = data.file.content
        }
    }
}

function viewStudentFileContent(userId, fileId) {
    studentCodeUrl = `/api/users/${userId}/files/${fileId}`
    displayStudentFileContent()
}

function openStudentProject(userId, projectId) {
    window.open(`/users/${userId}/projects/${projectId}`, '_blank').focus();
}

async function displayActiveProjects() {
    const response = await fetch("/api/admin/users")
    const users = await response.json()
    displayUserProjects(users)
    displayStudentFileContent()
}

function displayUserProjects(projects) {
    let result = ""
    const destinationElement = document.getElementById("active-projects")
    const users = [...new Set(projects.map(p => p.user_name))]
    for (let user of users) {
        const proj = projects.filter(p => p.user_name === user)
        const links = proj.map(p => `
            <div class="mb-2">
                <button class="btn btn-light" onclick="openStudentProject('${p.prj_id}', '${p.prj_id}')">Go to project</button>
                <button class="btn btn-light" onclick="viewStudentFileContent('${p.prj_id}', '${p.prj_id}')">View solution</button>
                <span>${p.prj_name}</span>
            </div>`
        ).join("")
        result += `
            <div class="card mb-2">
              <div class="card-body bg-info">
                <h5 class="card-title">${user}</h5>
                <p class="card-text">${links}</p>
              </div>
            </div>`
    }
    destinationElement.innerHTML = result
}

displayActiveProjects()
setInterval(displayActiveProjects, 10000)
