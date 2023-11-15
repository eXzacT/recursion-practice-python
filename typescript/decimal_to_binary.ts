// Decimal to binary number using recursion and iteration
import { tramp, Trampoline } from './global';

function decimalToBinary(num: number): string {
    let binary = '';
    while (num > 0) {
        const remainder = num % 2;
        num = Math.floor(num / 2);
        binary = remainder + binary;
    }
    return binary;
}

function decimalToBinaryRec(num: number): string {
    if (num == 0) {
        return ''
    }
    const remainder = num % 2;
    num = Math.floor(num / 2);
    return decimalToBinaryRec(num) + remainder;
}

function decimalToBinaryTailRec(num: number): string {
    function helper(num: number, binary = ''): string {
        if (num == 0) {
            return binary;
        }
        const remainder = num % 2;
        num = Math.floor(num / 2);
        return helper(num, remainder + binary);
    }
    return helper(num);
}

function decimalToBinaryThunk(num: bigint): Trampoline<string> {
    function helper(num: bigint, binary = ''): Trampoline<string> {
        if (num == 0n) {
            return binary;
        }
        const remainder = num % 2n;
        num = num / 2n;
        return () => helper(num, remainder + binary);
    }
    return helper(num);
}

const num = 101321009;

console.log(num.toString(2));
console.log(decimalToBinary(num));
console.log(decimalToBinaryRec(num));
console.log(decimalToBinaryTailRec(num));
//console.log(decimalToBinaryTailRec(2 ** 10_000));
console.log(tramp(decimalToBinaryThunk, 2n ** 10_000n));