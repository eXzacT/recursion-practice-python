// Mean of Array using Iteration and Recursion
import { Trampoline, tramp } from "./global";

function arrayMean(arr: number[]): number {
    let sum = 0;
    const length = arr.length;
    arr.forEach((val) => {
        sum += val;
    })
    return sum / length;
}

function arrayMeanRec(arr: number[]): number {
    const length = arr.length;
    function helper(idx: number): any {
        if (idx === length) {
            return 0
        }
        const curr = arr[idx];
        return curr + helper(idx + 1);
    }
    return helper(0) / length;
}

function arrayMeanTailRec(arr: number[]): number {
    const length = arr.length;
    function helper(idx: number, acc = 0): any {
        if (idx === length) {
            return acc / length;
        }
        const curr = arr[idx];
        return helper(idx + 1, acc + curr);
    }
    return helper(0);
}

function arrayMeanThunk(arr: number[]): Trampoline<number> {
    const length = arr.length;
    function helper(idx: number, acc = 0): Trampoline<number> {
        if (idx === length) {
            return acc / length;
        }
        const curr = arr[idx];
        return () => helper(idx + 1, acc + curr);
    }
    return helper(0);
}

const arr = Array.from({ length: 10 }, (_, i) => i + 1);
const long_arr = Array.from({ length: 10_000 }, (_, i) => i + 1);
console.log(arrayMean(arr));
console.log(arrayMeanRec(arr));
console.log(arrayMeanTailRec(arr));
//console.log(arrayMeanTailRec(long_arr));
console.log(tramp(arrayMeanThunk, long_arr));