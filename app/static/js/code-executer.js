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

