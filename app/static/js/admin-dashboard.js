let studentCodeUrl = ''
const codeAreaElement = document.getElementById("code-viewer")
codeAreaElement.value = ""

async function displayStudentFileContent() {
    if (studentCodeUrl){
        const request = await fetch(studentCodeUrl)
        if (request.status === 200) {
            const data = await request.json()
            codeAreaElement.value = data.files.map(f => f.content).join("\n")
        }
    }
}

function viewStudentFileContent(userId, projectId) {
    studentCodeUrl = `/api/users/${userId}/projects/${projectId}/files`
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
                <button class="btn btn-light" onclick="openStudentProject('${p.user_id}', '${p.prj_id}')">Go to project</button>
                <button class="btn btn-light" onclick="viewStudentFileContent('${p.user_id}', '${p.prj_id}')">View solution</button>
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

function syncStarterProjects() {
    fetch('/api/admin/sync-starter-projects')
}

function setListenerLogoutButton() {
    const button = document.getElementById('logout')
    button.addEventListener('click', (e) => {
        e.preventDefault()
        fetch('/api/admin/projects', { method: "DELETE" })
        window.location.pathname = `/admin/logout`;
    })
}

function keepLanguageEnvironmentsActive() {
    setInterval(() => fetch(`/api/admin/keep-language-environments-active`), 10000)
}

function main() {
    syncStarterProjects()
    displayActiveProjects()
    setInterval(displayActiveProjects, 10000)
    setListenerLogoutButton()
    keepLanguageEnvironmentsActive()
}

main()

