function applyRunCodeEvents() {
    const buttons = document.querySelectorAll("[data-execute-language]")
    for (const button of buttons) {
        button.addEventListener("click", event => {
            const action = runCodeActionFactory[button.dataset.executeLanguage]
            if (action) {
                action(button)
            }
        })
    }
}

async function runJavraScript(button) {
    const code = document.querySelector('[data-language=js]').value
    await fetch("/api/language/js/execute", {
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
    eval(code)
}

const runCodeActionFactory = {
    "js": runJavraScript,
}

applyRunCodeEvents()
