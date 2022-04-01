import * as codeInitializersFactory from './codeInitializers/codeInitializersFactory'

export function initialize(file) {
    const languageType = file.name.split(".").at(-1)
    const initializer = codeInitializersFactory.build(languageType)
    initializer && initializer()
}
