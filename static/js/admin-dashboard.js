async function getActiveProjects() {
    const response = await fetch("/admin/active-projects")
    const projects = await response.json()
    displayActiveExercises(projects)
}

function displayActiveExercises(exercises) {
    let result = ""
    const destinationElement = document.getElementById("active-exercises")
    const users = [...new Set(exercises.map(e => e.user))]
    for (let user of users) {
        const exerciseNumbers = exercises.filter(e => e.user === user).map(e => e.exerciseNumber)
        const links = exerciseNumbers.map(exNum => `
            <div>
                ${exNum}
                <button target="_blank" href="/exercises/${exNum}/${user}">Go to exercise</button>
                <button id="${user}-${exNum}">View solution</button>
            </div>`
        ).join("")
        result += `
            <div>
                <div class="user">${user}</div>
                <div class="links">${links}</div>
            </div>`
    }
    destinationElement.innerHTML = result
}

getActiveProjects()
setInterval(getActiveProjects, 10000)
