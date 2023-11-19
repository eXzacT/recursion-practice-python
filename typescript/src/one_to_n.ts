// Printing 1 to n iteratively and recursively
import { Trampoline, tramp } from "./global";
function oneToN(n: number): void {
    for (let idx = 0; idx < n; idx++) {
        console.log(idx);
    }
}

function oneToNTailRec(n: number): void {
    function helper(idx: number): void {
        if (idx == n) {
            return;
        }
        console.log(idx);
        return helper(idx + 1);
    }
    return helper(0);
}

function oneToNThunk(n: number): Trampoline<void> {
    function helper(idx: number): Trampoline<void> {
        if (idx == n) {
            return;
        }
        console.log(idx);
        return () => helper(idx + 1);
    }
    return helper(0);
}

oneToN(10);
oneToNTailRec(10);
tramp(oneToNThunk, 100_000);