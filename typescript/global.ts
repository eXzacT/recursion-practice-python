export type Trampoline<T> = T | (() => Trampoline<T>);

export function tramp<T>(fn: (...args: any[]) => Trampoline<T>, ...args: any[]): T {
    let result = fn(...args);
    while (result instanceof Function) {
        result = result();
    }
    return result;
}

export const alphabetString = Array.from({ length: 26 }, (_, idx) =>
    String.fromCharCode(idx + 97)).join('')