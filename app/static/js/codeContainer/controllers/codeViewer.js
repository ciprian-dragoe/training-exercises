let tabSize = 2
let languageType = ''

export function loadFile(file) {
    languageType = file.name.split(".").at(-1)
    const codeViewer = document.getElementById('code-viewer')
    codeViewer.value = file.content
    codeViewer.addEventListener("keydown", event => {
            const action = keyActionFactory[event.key]
            if (action) {
                action(codeViewer)
            }
    })
    codeViewer.focus()
}

function sendTab(codingArea) {
    const currentCursorPosition = codingArea.selectionStart
    codingArea.value = [
        codingArea.value.slice(0, codingArea.selectionStart),
        " ".repeat(tabSize),
        codingArea.value.slice(codingArea.selectionStart)]
        .join('')
    codingArea.selectionStart = currentCursorPosition + 2
    codingArea.selectionEnd = currentCursorPosition + 2
    setTimeout(() => codingArea.focus(), 0)
}

function sendEnter(codingArea) {
    setTimeout(() => {
        const currentCursorPosition = codingArea.selectionStart
        const cursorPosition = getCursorPosition(codingArea)
        const currentLine = codingArea.value.split("\n")[cursorPosition.lineNumber]
        const spacesPreviousLine = currentLine.length - currentLine.trimLeft().length
        const spacesFromNewBlockScope =
            currentLine.trimEnd().at(-1) === blockTypesFactory[languageType] ? tabSize : 0
        const newLineIndentation = " ".repeat(spacesPreviousLine + spacesFromNewBlockScope)
        codingArea.value = [
            codingArea.value.slice(0, currentCursorPosition),
            newLineIndentation,
            codingArea.value.slice(currentCursorPosition)]
            .join('')
        codingArea.selectionStart = currentCursorPosition + spacesPreviousLine + spacesFromNewBlockScope
        codingArea.selectionEnd = currentCursorPosition + spacesPreviousLine + spacesFromNewBlockScope
    }, 10)
}

function getCursorPosition(codingArea) {
    const currentPosition = codingArea.selectionStart - 1
    const lines = codingArea.value.split("\n")
    const result = {
        lineNumber: 0,
        colNumber: 0
    }
    let totalCharactersTraversed = 0
    for (let i=0; i<lines.length; i++) {
        result.lineNumber = i
        if (totalCharactersTraversed + lines[i].length + 1 > currentPosition) {
            result.colNumber = currentPosition - totalCharactersTraversed
            break
        }
        totalCharactersTraversed += lines[i].length + 1
    }

    return result
}

const keyActionFactory = {
    "Tab": sendTab,
    "Enter": sendEnter
}

const blockTypesFactory = {
    "js": "{",
    "py": ":",
    "css": "{",
    "html": ">",
    "sql": "*"
}
