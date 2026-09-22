import globals from 'globals'; // Import the globals package
import js from '@eslint/js'; // Import the ESLint JavaScript configuration
import {defineConfig} from 'eslint/config'; // Import the defineConfig function from ESLint
import stylistic from '@stylistic/eslint-plugin'; // Import the Stylistic ESLint plugin

export default defineConfig([
    {
        plugins: {
            '@stylistic': stylistic
        },
        languageOptions: {
            globals: {
                ...globals.browser,
                ...globals.commonjs,
                ...globals.jquery
            },
            parserOptions: {
                ...js.configs.recommended.parserOptions,
                ecmaVersion: 'latest',
                ecmaFeatures: {
                    impliedStrict: true
                },
                sourceType: 'module'
            }
        },
        rules: {
            ...js.configs.recommended.rules,
            ...stylistic.configs.recommended.rules,
            // https://eslint.style/rules/arrow-parens
            '@stylistic/arrow-parens': ['error', 'always'],
            // https://eslint.style/rules/brace-style
            '@stylistic/brace-style': ['error', '1tbs', {
                allowSingleLine: false
            }],
            // https://eslint.style/rules/comma-dangle
            '@stylistic/comma-dangle': ['error', 'never'],
            // https://eslint.style/rules/indent
            '@stylistic/indent': ['error', 4, {
                SwitchCase: 1
            }],
            // https://eslint.style/rules/indent-binary-ops
            '@stylistic/indent-binary-ops': ['error', 4],
            // https://eslint.style/rules/object-curly-spacing
            '@stylistic/object-curly-spacing': ['error', 'never'],
            // https://eslint.style/rules/quotes
            '@stylistic/quotes': ['error', 'single', {
                allowTemplateLiterals: 'avoidEscape',
                avoidEscape: true
            }],
            // https://eslint.style/rules/semi
            '@stylistic/semi': ['error', 'always'],
            // https://eslint.style/rules/space-before-function-paren
            '@stylistic/space-before-function-paren': ['error', {
                anonymous: 'always',
                asyncArrow: 'always',
                catch: 'always',
                named: 'always'
            }]
        }
    }
]);
