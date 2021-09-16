const tabSize = 2

function applyCodingInputEvents() {
    const codingAreas = document.querySelectorAll("[data-language]")
    for (const codingArea of codingAreas) {
        getExistingCode(codingArea)
        codingArea.addEventListener("keydown", event => {
            const action = keyActionFactory[event.key]
            if (action) {
                action(codingArea)
            }
        })
    }

    codingAreas.length === 1 && codingAreas[0].focus()
}

async function getExistingCode(codeArea) {
    const request = await fetch(`/api/language/${codeArea.dataset.language}/read/${document.body.dataset.user}/${document.body.dataset.exerciseNumber}`)
    if (request.status === 200) {
        const data = await request.json()
        codeArea.value = data.code
    }
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
            currentLine.trimRight().at(-1) === blockTypesFactory[codingArea.dataset.language] ? tabSize : 0
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
    "py": ":"
}



applyCodingInputEvents()
