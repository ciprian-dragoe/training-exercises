function runSql(code, result) {
    if (result.error) {
        printHtmlElement("query-result", buildErrorMessage(result.error))
    } else {
        printHtmlElement("query-result", buildTable(result.output, "MyQuery"))
    }
    printHtmlElement("query-result", buildTable(result.output, "MyQuery"))
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
    if (!tableData.length) {
        return '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Querry returned no elemnts'
    }
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
    let data = await executeCodeRemotely(sqlCode, "sql")
    addHtmlElement(placementId, buildTable(data.output, tableName))
}

async function displayDefaultTables() {
    await appendQueryTable("initial-data", "select * from addresses", 'addresses')
    await appendQueryTable("initial-data", "select * from clients", 'clients')
    await appendQueryTable("initial-data", "select * from products", 'products')
    await appendQueryTable("initial-data", "select * from products_price_history", 'products_price_history')
    addTableEvents()
}

function addTableEvents() {
    document.querySelectorAll("td").forEach(item => {
        item.addEventListener("click", (e) => {
            toggleClass(e, "red")
        })
        item.addEventListener("contextmenu", (e) => {
            e.preventDefault()
            toggleClass(e, "green")
        })
    })
}

function toggleClass(domItem, className) {
    if (domItem.target.classList.length) {
        domItem.target.className.includes(className) ? domItem.target.className = "" : domItem.target.className = className
    } else {
        domItem.target.className = className
    }
}

displayDefaultTables()
