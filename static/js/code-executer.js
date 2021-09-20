function applyRunCodeEvents() {
    const buttons = document.querySelectorAll("[data-execute-language]")
    for (const button of buttons) {
        button.addEventListener("click", event => runCode(button))
    }
}

async function runCode(button) {
    const language = button.dataset.executeLanguage
    const code = document.querySelector(`[data-language=${language}]`).value
    const result = await executeCodeRemotely(code, language)
    const callback = window[button.dataset.executeCallback]
    callback && callback(code, result)
}

async function executeCodeRemotely(code, language) {
    const request = await fetch(`/api/language/${language}/execute`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            code,
            exerciseNumber: document.body.dataset.exerciseNumber,
            user: document.body.dataset.user
        })
    })
    return await request.json()
}

applyRunCodeEvents()
