
async function getProjectFiles(userId, projectId) {
    const request = await fetch(`/api/users/${userId}/projects/${projectId}/files`)
    return await request.json()
}

async function runCode(button) {
    const codeResult = document.getElementById("code-result")
    codeResult ? codeResult.innerHTML = "" : 0
    const language = button.dataset.executeLanguage
    const code = document.querySelector(`[data-language=${language}]`).value
        .replaceAll(/î/g, 'i')
        .replaceAll(/Î/g, 'I')
        .replaceAll(/ă/g, 'a')
        .replaceAll(/Ă/g, 'A')
        .replaceAll(/Ț/g, 't')
        .replaceAll(/ț/g, 't')
        .replaceAll(/â/g, 'a')
        .replaceAll(/Â/g, 'A')
        .replaceAll(/Ș/g, 'S')
        .replaceAll(/ș/g, 's')
    button.disabled = true
    const result = await executeCodeRemotely(language, code, button.dataset.userId, button.dataset.fileId)
    button.disabled = false
    const callback = window[button.dataset.executeCallback]
    callback && callback(code, result)
}

async function executeCodeRemotely(language, code, userId, fileId) {
    const request = await fetch(`/api/language/${language}/execute`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            code,
            file_id: fileId,
            user_id: userId
        })
    })
    return await request.json()
}


export async function attachExecuteCodeCallback() {
    const projectId = window.location.href.split("/")[6]
    const userId = window.location.href.split("/")[4]
    const buttons = document.querySelectorAll("[data-execute-language]")

    getProjectFiles(userId, projectId).then(result => {
        for (let i=0; i < buttons.length; i++) {
            buttons[i].dataset.fileId = result.files[i].id
            buttons[i].dataset.userId = userId
            buttons[i].addEventListener("click", event => runCode(buttons[i]))
        }
    })
}

