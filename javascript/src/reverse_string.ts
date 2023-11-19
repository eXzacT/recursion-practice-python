// Print reverse of a string using iteration & recursion
import { alphabetString, tramp, Trampoline } from "./global"

function reverseString(s: string): string {
    let reversedString = ''
    for (const c of s) {
        reversedString = c + reversedString
    }
    return reversedString
}

function reverseStringRec(s: string): string {
    const length = s.length
    function helper(idx: number): string {
        if (idx == length - 1) {
            return s[idx]
        }
        return helper(idx + 1) + s[idx]
    }
    return helper(0)
}

function reverseStringTailRec(s: string): string {
    const length = s.length
    function helper(idx: number, acc = ''): string {
        if (idx == length) {
            return acc
        }
        return helper(idx + 1, s[idx] + acc)
    }
    return helper(0)
}

function reverseStringThunk(s: string): Trampoline<string> {
    const length = s.length
    function helper(idx: number, acc = ''): Trampoline<string> {
        if (idx == length) {
            return acc
        }
        return () => helper(idx + 1, s[idx] + acc)
    }
    return helper(0)
}


const repeatedAlphabet = alphabetString.repeat(10_000)
console.log(reverseString(alphabetString))
console.log(reverseStringRec(alphabetString))
console.log(reverseStringTailRec(alphabetString))
//console.log(reverseStringTailRec(repeatedAlphabet))
console.log(tramp(reverseStringThunk, repeatedAlphabet))