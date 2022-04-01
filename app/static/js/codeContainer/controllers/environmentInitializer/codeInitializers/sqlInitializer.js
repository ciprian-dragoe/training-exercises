import * as language from '../../../data/language.js'
import * as displayErrorMessage from '../../../view/displayErrorMessage.js'
import * as displayTable from '../../../view/displayTable.js'
import * as displayDemoTable from "../../../view/displayDemoTable.js";

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
