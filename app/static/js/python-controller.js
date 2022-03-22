function runPython(code, result) {
    const destinationElement = document.getElementById("code-result")
    if (result.error) {
        destinationElement.innerHTML = `<div style="color: red">${replaceWhiteSpace(result.error)}</div>`
    } else {
        destinationElement.innerHTML = `<div>${replaceWhiteSpace(result.output)}</div>`
    }
}

function replaceWhiteSpace(input) {
    return input.replaceAll('\\n', '</br>')
}
