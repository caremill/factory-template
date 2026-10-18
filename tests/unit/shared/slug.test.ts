import { describe, expect, it } from 'vitest';

import { slugify } from '../../../src/shared/slug.js';

describe('slugify', () => {
  it('lowercases and joins words with hyphens', () => {
    expect(slugify('Practice Waitlist')).toBe('practice-waitlist');
  });

  it('transliterates German umlauts and ß', () => {
    expect(slugify('Übersicht für Größe')).toBe('uebersicht-fuer-groesse');
  });

  it('strips accents from other Latin letters', () => {
    expect(slugify('Café São Paulo')).toBe('cafe-sao-paulo');
  });

  it('collapses punctuation and trims leading and trailing separators', () => {
    expect(slugify('  --Hello,   World!--  ')).toBe('hello-world');
  });

  it('returns an empty string when nothing URL-safe remains', () => {
    expect(slugify('!!!')).toBe('');
  });
});
