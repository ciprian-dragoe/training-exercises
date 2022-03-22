let studentCodeUrl = ''
const codeAreaElement = document.getElementById("code-viewer")
codeAreaElement.value = ""

async function displayStudentCode() {
    if (studentCodeUrl){
        const request = await fetch(studentCodeUrl)
        if (request.status === 200) {
            const data = await request.json()
            codeAreaElement.value = data.code
        }
    }
}

function setStudentCodeFetchHook(user, exNum) {
    console.log(user, exNum)
    const language = exNum.split("_")[1]
    studentCodeUrl = `/api/language/${language}/read/${user}/${exNum}`
    displayStudentCode()
}

function viewStudentCodingArea(user, exNum) {
    window.open(`/exercises/${exNum}/${user}`, '_blank').focus();
}

async function displayActiveProjects() {
    const response = await fetch("/admin/active-projects")
    const projects = await response.json()
    displayActiveExercises(projects)
    displayStudentCode()
}

function displayActiveExercises(exercises) {
    let result = ""
    const destinationElement = document.getElementById("active-exercises")
    const users = [...new Set(exercises.map(e => e.user))]
    for (let user of users) {
        const exerciseNumbers = exercises.filter(e => e.user === user).map(e => e.exerciseNumber)
        const links = exerciseNumbers.map(exNum => `
            <div class="mb-2">
                <button class="btn btn-light" onclick="viewStudentCodingArea('${user}', '${exNum}')">Go to exercise</button>
                <button class="btn btn-light" onclick="setStudentCodeFetchHook('${user}', '${exNum}')">View solution</button>
                <span>${exNum}</span>
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
