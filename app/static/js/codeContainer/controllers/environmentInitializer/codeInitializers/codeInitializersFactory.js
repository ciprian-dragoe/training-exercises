import * as sqlInitializer from './sqlInitializer'

const factory = {
    'sql': sqlInitializer.initialize
}

export function build(languageType) {
    return factory[languageType]
}
