import { describe, expect, it } from 'vitest';

import { untested } from '../../../src/shared/gate-check.js';
describe('untested', () => {
  it('doubles values above 10', () => {
    expect(untested(11)).toBe(22);
  });

  it('subtracts one otherwise', () => {
    expect(untested(10)).toBe(9);
  });
});
