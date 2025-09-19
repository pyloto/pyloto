module.exports = {
  root: true,
  extends: ['next', 'next/core-web-vitals', 'plugin:@typescript-eslint/recommended', 'prettier'],
  plugins: ['@typescript-eslint'],
  parser: '@typescript-eslint/parser',
  parserOptions: { ecmaVersion: 2020, sourceType: 'module' },
  rules: {
    'react-hooks/exhaustive-deps': 'warn',
    '@typescript-eslint/consistent-type-imports': 'warn',
    '@typescript-eslint/no-unused-vars': ['warn', { argsIgnorePattern: '^_', varsIgnorePattern: '^_' }],
  },
  overrides: [
    {
      files: ['src/components/sections/CTA.tsx'],
      rules: {
        // Permite ALLCAPS para este componente específico evitando falso positivo
        'react/jsx-pascal-case': ['off']
      }
    }
  ]
}
