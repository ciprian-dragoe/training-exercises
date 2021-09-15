const codeElement = document.getElementById("code-area")
const runElement = document.getElementById("run-code")
const tabSize = 2
codeElement.focus()

codeElement.addEventListener("keydown", event => {
    const action = keyAction[event.key]
    if (action) {
        action()
    }
})

function sendTab() {
    const currentCursorPosition = codeElement.selectionStart
    codeElement.value = [
        codeElement.value.slice(0, codeElement.selectionStart),
        " ".repeat(tabSize),
        codeElement.value.slice(codeElement.selectionStart)]
        .join('')
    codeElement.selectionStart = currentCursorPosition + 2
    codeElement.selectionEnd = currentCursorPosition + 2
    setTimeout(() => codeElement.focus(), 0)
}

function sendEnter() {
    setTimeout(() => {
        const currentCursorPosition = codeElement.selectionStart
        const cursorPosition = getCursorPosition(codeElement)
        const currentLine = codeElement.value.split("\n")[cursorPosition.lineNumber]
        const spacesPreviousLine = currentLine.length - currentLine.trimLeft().length
        const spacesFromNewBlockScope = currentLine.trimRight().at(-1) === "{" ? 2 : 0
        const newLineIndentation = " ".repeat(spacesPreviousLine + spacesFromNewBlockScope)
        codeElement.value = [
            codeElement.value.slice(0, currentCursorPosition),
            newLineIndentation,
            codeElement.value.slice(currentCursorPosition)]
            .join('')
        codeElement.selectionStart = currentCursorPosition + spacesPreviousLine + spacesFromNewBlockScope
        codeElement.selectionEnd = currentCursorPosition + spacesPreviousLine + spacesFromNewBlockScope
    }, 0)
}

function getCursorPosition(inputElement) {
    const currentPosition = inputElement.selectionStart - 1
    const lines = codeElement.value.split("\n")
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

const keyAction = {
    "Tab": sendTab,
    "Enter": sendEnter
}
