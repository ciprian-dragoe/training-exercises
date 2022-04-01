import * as language from '../../data/language'
import * as codeParserCallbackFactory from './codeParserCallbacks/codeParserCallbackFactory'

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

export function attachEventListener(project, file) {
    const button = document.getElementById("code-runner")
    const languageType = file.name.split(".").at(-1)
    button.innerText = `Run ${languageType}`
    const resultParserCallBack = codeParserCallbackFactory.build(languageType)
    button.addEventListener('click', async () => {
        const code = document.getElementById("code-area").value
        button.disabled = true
        const result = await language.updateFileAndRunCode(languageType, code, project.user_id, file.id)
        button.disabled = false
        resultParserCallBack(code, result)
    })
}
