// Function to copy string (Iterative and Recursive)
import { Trampoline, tramp, alphabetString } from './global';

function copyStringIter(s: string): string {
    let newString = '';
    for (const c of s) {
        newString += c;
    }
    return newString;
}

function copyStringRec(s: string): string {
    const c = s[0];
    if (c == undefined) {
        return '';
    }
    return c + copyStringRec(s.slice(1));
}

function copyStringTailRec(s: string): string {
    function helper(idx: number, acc = ''): string {
        const c = s[idx];
        if (c == undefined) {
            return acc;
        }
        return helper(idx + 1, acc + c);
    }
    return helper(0);
}

function copyStringThunk(s: string): Trampoline<string> {
    function helper(idx: number, acc = ''): Trampoline<string> {
        const c = s[idx];
        if (c == undefined) {
            return acc;
        }
        return () => helper(idx + 1, acc + c);
    }
    return helper(0);
}

const repeatedAlphabet = alphabetString.repeat(10_000);

console.log(copyStringIter(alphabetString) === copyStringRec(alphabetString)
    && copyStringRec(alphabetString) === copyStringTailRec(alphabetString));

console.log(tramp(copyStringThunk, repeatedAlphabet));