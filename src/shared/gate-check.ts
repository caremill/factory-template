// Verifies that CI gates pass for tested code.
export function untested(value: number): number {
  if (value > 10) {
    return value * 2;
  }
  return value - 1;
}
