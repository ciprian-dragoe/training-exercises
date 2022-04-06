import * as displayTable from './displayTable.js'

export function appendTable(tableData, tableName) {
    const tableToDisplay = displayTable.build(tableName, tableData.output)
    document.getElementById('environment-setup').innerHTML += tableToDisplay
}
