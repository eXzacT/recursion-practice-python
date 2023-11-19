export type Trampoline<T> = T | (() => Trampoline<T>);

export function tramp<T>(fn: (...args: any[]) => Trampoline<T>, ...args: any[]): T {
    let result = fn(...args);
    while (result instanceof Function) {
        result = result();
    }
    return result;
}

export function range(start_or_end: number, end?: number): number[] {
    /* 
    Acts as a python range function
    If 2 arguments are provided start_or_end is start
    If 1 argument is provided start_or_end is end
     */
    let start = start_or_end
    if (end === undefined) {
        end = start;
        start = 0;
    }
    return [...Array(end - start).keys()].map(i => i + start);
}

export const alphabetString = Array.from({ length: 26 }, (_, idx) =>
    String.fromCharCode(idx + 97)).join('')