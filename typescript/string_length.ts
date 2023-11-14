// Length of a string using iteration and recursion
import { Trampoline, tramp, alphabetString } from "./global";


function stringLength(s: string,): number {
    let counter = 0;
    for (const _ of s) {
        counter += 1;
    }
    return counter;
}

function stringLengthRec(s: string): number {
    function helper(idx: number): number {
        if (s[idx] === undefined) {
            return 0;
        }
        return 1 + helper(idx + 1);
    }
    return helper(0);
}

function stringLengthTailRec(s: string): number {
    function helper(idx: number): number {
        if (s[idx] === undefined) {
            return idx;
        }
        return helper(idx + 1);
    }
    return helper(0);
}


function stringLengthThunk(s: string): Trampoline<number> {
    function helper(idx: number): Trampoline<number> {
        if (s[idx] === undefined) {
            return idx;
        }
        return () => helper(idx + 1);
    }
    return helper(0);
}

const repeatedAlphabet = alphabetString.repeat(10_000);

console.log(stringLength(alphabetString));
console.log(stringLengthRec(alphabetString));
console.log(stringLengthTailRec(alphabetString));
// console.log(stringLengthTailRec(repeated_alphabet));
console.log(tramp(stringLengthThunk,
    repeatedAlphabet));