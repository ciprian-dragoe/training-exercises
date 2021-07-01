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

async function executeQuery() {
    const response = await fetch("/sql/execute", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            query: textArea.value,
            user: document.body.dataset.user,
            exerciseNumber: document.body.dataset.exerciseNumber,
        })
    })
    const data = await response.json()
    response.status === 200 ? buildTable("query-result", data) : writeError(data, "query-result")
}

function writeError(errorMessage, placementId) {
    const reportingZone = document.getElementById(placementId)
    reportingZone.innerHTML = `
    <div class="error">
        ${errorMessage}
    </div>
`
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

function buildTable(placementId, tableData) {
    const tableHeaders = Object.keys(tableData[0])
    const table = document.getElementById(placementId)
    table.innerHTML = `
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

document.getElementById("run-query-button").addEventListener("click", executeQuery)