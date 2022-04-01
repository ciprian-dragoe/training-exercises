import * as language from '../../../data/language'
import * as displayErrorMessage from '../../../view/displayErrorMessage'
import * as displayTable from '../../../view/displayTable'
import * as displayDemoTable from "../../../view/displayDemoTable";

async function appendQueryTable(tableName, sqlCode) {
    const data = await language.runCode('sql', sqlCode)
    if (data.error) {
        displayErrorMessage.show(data.error)
    }
    displayDemoTable.appendTable(data, tableName)
}

export async function initialize() {
    await appendQueryTable( 'addresses', "select * from addresses")
    await appendQueryTable( 'clients', "select * from clients")
    await appendQueryTable( 'products', "select * from products")
    await appendQueryTable( 'products_price_history', "select * from products_price_history")
    displayTable.addTableEvents()
}
