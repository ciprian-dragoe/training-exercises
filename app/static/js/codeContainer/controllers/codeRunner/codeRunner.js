import * as language from '../../data/language.js'
import * as codeParserCallbackFactory from './codeParserCallbacks/codeParserCallbackFactory.js'

export function attachEventListener(project, file) {
    const button = document.getElementById("code-runner")
    const languageType = file.name.split(".").at(-1)
    button.innerText = `Run ${languageType}`
    const resultParserCallBack = codeParserCallbackFactory.build(languageType)
    button.addEventListener('click', async () => {
        const code = document.getElementById("code-viewer").value
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
        const result = await language.updateFileAndRunCode(languageType, code, project.user_id, file.id)
        button.disabled = false
        resultParserCallBack(code, result)
    })
}
