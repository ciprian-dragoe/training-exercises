console.log(11)
let timerID
const textArea = document.getElementById("sql")


textArea.addEventListener("input", (e) => {
    timerID && clearTimeout(timerID)

    timerID = setTimeout(() => {
        const formattedSql = sqlFormatter.format(textArea.value, {
            language: "postgresql",
            uppercase: true,
          });
        textArea.value = formattedSql
    }, 1000)
})

async function getPostResult(data) {
    return await fetch("/sql/execute", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
}

async function executeQuery() {
    const response = await getPostResult({
            query: textArea.value,
            user: document.body.dataset.user,
            exerciseNumber: document.body.dataset.exerciseNumber,
        })
    const data = await response.json()
    if (response.status === 200) {
        printHtmlElement("query-result", buildTable(data))
    } else {
        printHtmlElement("query-result", buildErrorMessage(data))
    }
}

function buildErrorMessage(errorMessage) {
    return `<div class="error">
        ${errorMessage}
    </div>`
}

function generateHtmlTableHeaders(headers) {
    let result = ""
    headers.forEach(header => {
        result = result + `<td>${header}</td>`
    })
    return "<tr>" + result + "</tr>"
}

function generateHtmlTableBody(items) {
    let result = ""
    items.forEach(item => {
        let row = ""
        Object.values(item).forEach(cell => {
            row = row + `<td>${cell}</td>`
        })
        result = result + `<tr>${row}</tr>`
    })
    return result
}

function printHtmlElement(placementId, htmlElement) {
    document.getElementById(placementId).innerHTML = htmlElement
}

function addHtmlElement(placementId, htmlElement) {
    document.getElementById(placementId).innerHTML += htmlElement
}

function buildTable(tableData) {
    const tableHeaders = Object.keys(tableData[0])
    return `
<table class="table table-striped table-hover">
    <thead>
        ${generateHtmlTableHeaders(tableHeaders)}
    </thead>
    <tbody>
        ${generateHtmlTableBody(tableData)}
    </tbody>
</table>
    `
}

async function displayDefaultTables() {
    let response = await getPostResult({ query: "select * from clients" })
    const clients = await response.json()
    addHtmlElement("initial-data", buildTable(clients))
    response = await getPostResult({ query: "select * from products" })
    const products = await response.json()
    addHtmlElement("initial-data", buildTable(products))
}


document.getElementById("run-query-button").addEventListener("click", executeQuery)
displayDefaultTables()