// Sum of first n numbers
import { Trampoline, tramp } from "./global";

function sum(n: number): number {
    return n * (n + 1) / 2;
}

function sumIterative(n: number): number {
    let sum = 0;
    while (n > 0) {
        sum += n;
        n--;
    }
    return sum;
}

function sumRec(n: number): number {
    if (n === 0) {
        return 0;
    }
    return n + sumRec(n - 1);
}

function sumTailRec(n: number): number {
    function helper(n: number, acc = 0): number {
        if (n === 0) {
            return acc;
        }
        return helper(n - 1, n + acc);
    }
    return helper(n);
}

function sumThunk(n: number): Trampoline<number> {
    function helper(n: number, acc = 0): Trampoline<number> {
        if (n === 0) {
            return acc;
        }
        return () => helper(n - 1, n + acc);
    }
    return helper(n);
}

console.log(sum(10));
console.log(sumIterative(10));
console.log(sumRec(10));
console.log(sumTailRec(10));
//console.log(sumTailRec(10_000));
console.log(tramp(sumThunk, 10_000));