import * as displayErrorMessage from "../../../view/displayErrorMessage";
import * as displayRunCodeResult from "../../../view/displayRunCodeResult";
import * as displayTable from "../../../view/displayTable";

const factory = {
    js: jsParser,
    sql: sqlParser,
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

