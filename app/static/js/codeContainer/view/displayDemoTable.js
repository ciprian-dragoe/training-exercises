import * as displayTable from './displayTable'

export function appendTable(tableData, tableName) {
    const tableToDisplay = displayTable.build(tableName, tableData)
    document.getElementById('environment-setup').innerHTML += tableToDisplay
}
