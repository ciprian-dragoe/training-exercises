import * as sqlInitializer from './sqlInitializer.js'

const factory = {
    'sql': sqlInitializer.initialize
}

export function build(languageType) {
    return factory[languageType]
}
