// Find first uppercase character iteratively and recursively
import { Trampoline, tramp, alphabetString } from './global';

function findFirstUppercaseLetter(s: string): { idx: number, c: string } | null {
    for (const [idx, c] of Array.from(s).entries()) {
        if (c.toUpperCase() == c && c.toLowerCase() != c) {
            return { idx, c };
        }
    }
    return null;
}

type Result = { idx: number, c: string } | null;

function findFirstUppercaseLetterTailRec(s: string): Result {
    function helper(idx: number): Result {
        const c = s[idx];
        if (c == undefined) {
            return null;
        }
        if (c.toUpperCase() == c && c.toLowerCase() != c) {
            return { idx, c };
        }
        return helper(idx + 1);
    }
    return helper(0);
}

function findFirstUppercaseLetterThunk(s: string): Trampoline<Result> {
    function helper(idx: number): Trampoline<Result> {
        const c = s[idx];
        if (c == undefined) {
            return null;
        }
        if (/[A-Z]/.test(c)) {
            return { idx, c };
        }
        return () => helper(idx + 1);
    }
    return helper(0);
}

const lowercase = 'helloworld';
const uppercase = 'helloWorld';

console.log(findFirstUppercaseLetter(lowercase));
console.log(findFirstUppercaseLetter(uppercase));
console.log(findFirstUppercaseLetterTailRec(lowercase));
console.log(findFirstUppercaseLetterTailRec(uppercase));

const repeatedAlphabet = alphabetString.repeat(10_000);
const repeatedAlphabetOneUppercase = repeatedAlphabet + 'Z';
console.log(tramp(findFirstUppercaseLetterThunk, repeatedAlphabet));
console.log(tramp(findFirstUppercaseLetterThunk, repeatedAlphabetOneUppercase));