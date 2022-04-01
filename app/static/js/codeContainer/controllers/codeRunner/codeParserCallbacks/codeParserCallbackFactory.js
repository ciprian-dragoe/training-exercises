import * as displayErrorMessage from "../../../view/displayErrorMessage.js";
import * as displayRunCodeResult from "../../../view/displayRunCodeResult.js";
import * as displayTable from "../../../view/displayTable.js";

const factory = {
    js: jsParser,
    sql: sqlParser,
    py: pyParser,
    html: htmlParser,
    css: cssParser
}

export function build(languageType) {
    return factory[languageType]
}

function jsParser (code, result) {
    eval(code)
}

function sqlParser(code, result) {
    if (result.error) {
        displayErrorMessage.show(result.error)
    } else {
        const table = displayTable.build("MyQuery", result.output)
        displayRunCodeResult.show(table)
    }
}

function pyParser(code, result) {
    if (result.error) {
        displayErrorMessage.show(result.error)
    } else {
        displayRunCodeResult.show(result.output.replaceAll('\\n', '</br>'))
    }
}

function htmlParser(code, result) {
    if (result.error) {
        displayErrorMessage.show(result.error)
    } else {
        displayRunCodeResult.show(result.output.replaceAll('\\n', '</br>'))
    }
}

function cssParser(code, result) {
    if (result.error) {
        displayErrorMessage.show(result.error)
    } else {
        displayRunCodeResult.show(`<style>${result.output.replaceAll('\\n', '</br>')}</style>`)
    }
}
