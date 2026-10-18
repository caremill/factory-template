/**
 * Turns a title into a stable, URL-safe slug, e.g. for `/de/praxis/warteliste`.
 * German umlauts and ß are transliterated so URLs stay readable.
 */
export function slugify(input: string): string {
  return input
    .trim()
    .toLowerCase()
    .replaceAll('ä', 'ae')
    .replaceAll('ö', 'oe')
    .replaceAll('ü', 'ue')
    .replaceAll('ß', 'ss')
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}
