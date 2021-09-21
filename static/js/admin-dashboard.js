console.log("mege")

async function getActiveProjects() {
    const response = await fetch("/admin/active-projects")
    const projects = await response.json()
    displayActiveExercises(projects)
}

function displayActiveExercises(exercises) {
    const destinationElement = document.getElementById("active-exercises")
    let result = ""
    for (let exercise of exercises) {
        result += `
        <div><a href="/exercises/${exercise.exerciseNumber}/${exercise.user}">
            ${exercise.user} - ${exercise.exerciseNumber.replaceAll("_", " ")}
        </a></div>`
    }
    destinationElement.innerHTML = result
}

setInterval(getActiveProjects, 10000)
