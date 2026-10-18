import { defineConfig } from 'vitest/config';

// Coverage thresholds are a quality gate. Changing them is a high-risk change (see CODEOWNERS).
const STRICT = { lines: 90, functions: 90, branches: 90, statements: 90 };

export default defineConfig({
  test: {
    include: ['tests/unit/**/*.test.ts'],
    coverage: {
      provider: 'v8',
      include: ['src/**/*.ts'],
      reporter: ['text', 'cobertura', 'lcov'],
      reportsDirectory: 'coverage',
      thresholds: {
        lines: 80,
        functions: 80,
        branches: 80,
        statements: 80,
        // Critical domain modules need a higher bar.
        'src/**/consent/**': STRICT,
        'src/**/matching/**': STRICT,
        'src/**/safeguarding/**': STRICT,
        'src/**/scheduling/**': STRICT,
      },
    },
  },
});
