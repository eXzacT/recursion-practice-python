import { range, Trampoline, tramp } from './global';

function fibonacciIter(n: number): number {
    let a = 0;
    let b = 1;

    // Since all the numbers before 0 are zeros we can return 0
    if (n <= 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }

    // 'a' is updated to the previous 'b' each iteration.
    // Running 'n' times gives the 'n-th' and 'n+1-th' Fibonacci number.
    // Since we are interested in 'a', we can also run n-1 times and return 'b'
    for (const _ of range(n - 1)) {
        [a, b] = [b, a + b];
    }
    return b;
}

function fibonacciRec(n: number): number {
    // return 1 for 1 and 0 for everything else below 1
    if (n <= 1) {
        return n;
    }
    return fibonacciRec(n - 1) + fibonacciRec(n - 2);
}

function fibonacciTailRec(n: number): number {
    // Not passing a copy of n since we don't care about changing it
    function helper(curr = 0, nxt = 1): number {
        if (n <= 0) {
            return curr;
        }
        // It would work without this if but that's 1 extra loop
        if (n < 1) {
            return nxt;
        }
        n--;
        return helper(nxt, curr + nxt);
    }
    return helper();
}
function fibonacciThunk(n: number): Trampoline<number> {
    function helper(curr = 0, nxt = 1): Trampoline<number> {
        if (n <= 0) {
            return curr;
        }
        if (n < 1) {
            return nxt;
        }
        n--;
        return () => helper(nxt, curr + nxt);
    }
    return helper();
}

function fibonacciThunkBigint(n: bigint): Trampoline<bigint> {
    function helper(curr = 0n, nxt = 1n): Trampoline<bigint> {
        if (n <= 0n) {
            return curr;
        }
        if (n < 1n) {
            return nxt;
        }
        n--;
        return () => helper(nxt, curr + nxt);
    }
    return helper(n);
}

console.log(Array.from({ length: 7 }, (_, idx) => fibonacciIter(idx)).join(' '));
//val and idx are same (val,idx) so we can use just val instead
console.log([...Array(7).keys()].map(val => fibonacciRec(val)).join(' '));
//val and idx are not the same in this case, val will be 5 and idx 0
console.log(Array.from(range(5, 7), val => fibonacciTailRec(val)).join(' '));
console.log(range(7).map(val => tramp(fibonacciThunk, val)).join(' '));
//console.log(fibonacciTailRec(100_000));
console.log(tramp(fibonacciThunkBigint, 100_000n));



