function runCss(code, result) {
    const destinationElement = document.getElementById("code-result")
    if (result.error) {
        destinationElement.innerHTML = `<style>${result.output}</style>`
    } else {
        destinationElement.innerHTML = `<style>${replaceWhiteSpace(result.output)}</style>`
    }
}

function replaceWhiteSpace(input) {
    return input.replaceAll('\\n', '</br>')
}
