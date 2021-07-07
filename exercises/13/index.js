console.log("show all the clients who do not have an address")
const user = document.body.dataset.user
const exerciseNumber = document.body.dataset.exerciseNumber
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
    }, 1500)
})

async function getPostResult(data) {
    return await fetch("/api/sql/execute", {
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
            user: user,
            exerciseNumber: exerciseNumber,
        })
    const data = await response.json()
    if (response.status === 200) {
        printHtmlElement("query-result", buildTable(data, "MyQuery"))
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

function buildTable(tableData, tableName) {
    const tableHeaders = Object.keys(tableData[0])
    return `
<div class="table">
    <h4 class="text-center">${tableName}</h4>
    <table class="table table-striped table-hover">
        <thead>
            ${generateHtmlTableHeaders(tableHeaders)}
        </thead>
        <tbody>
            ${generateHtmlTableBody(tableData)}
        </tbody>
    </table>
</div>
    `
}

async function appendQueryTable(placementId, sqlCode, tableName) {
    let response = await getPostResult({ query: sqlCode })
    const data = await response.json()
    addHtmlElement(placementId, buildTable(data, tableName))
}

async function displayDefaultTables() {
    await appendQueryTable("initial-data", "select * from addresses", 'addresses')
    await appendQueryTable("initial-data", "select * from clients", 'clients')
    await appendQueryTable("initial-data", "select * from products", 'products')
    await appendQueryTable("initial-data", "select * from products_price_history", 'products_price_history')
    addTableEvents()
    const response = await fetch(`/api/sql/${user}/${exerciseNumber}`)
    if (response.status === 200) {
        const data = await response.json()
        textArea.value = data.query
        data && executeQuery()
    }
}

function addTableEvents() {
    document.querySelectorAll("td").forEach(item => {
        item.addEventListener("click", (e) => {
            e.target.classList.toggle("red")
        })
        item.addEventListener("contextmenu", (e) => {
            e.preventDefault()
            e.target.classList.toggle("green")
        })
    })
}

document.getElementById("run-query-button").addEventListener("click", executeQuery)
displayDefaultTables()