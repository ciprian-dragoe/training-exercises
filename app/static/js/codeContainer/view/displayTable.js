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

function toggleClass(domItem, className) {
    if (domItem.target.classList.length) {
        domItem.target.className.includes(className) ? domItem.target.className = "" : domItem.target.className = className
    } else {
        domItem.target.className = className
    }
}

// todo: add table events after returning a table from code execution
export function addTableEvents() {
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

export function build(tableName, tableData) {
    if (!tableData.length) {
        return '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Query returned no elements'
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
