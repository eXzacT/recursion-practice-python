// All possible combinations of n elements from a given array
function generateNSizedSets(n: number, arr: number[]): number[][] {
    const res: number[][] = [];
    const len = arr.length;
    const possible_combinations = 1 << len; // Same as 2^len

    // The issue with this approach is there is a lot of empty work
    // We only care about i with binary representation of n 1's
    // So for n=3 we want 1110,1101, 1011 and 0111
    // We can make it a bit faster by starting from i=n not 0
    for (let i = n; i < possible_combinations; i++) {
        const set: number[] = [];
        for (let j = 0; j < len; j++) {
            // If j-th bit in i is set, add arr[j] to the combination
            if ((i & (1 << j)) !== 0) {
                set.push(arr[j]);
            }
        }

        // If the combination size is n, add it to the result
        if (set.length === n) {
            res.push(set);
        }
    }

    return res;
}

function generateNSizedSetsV2(n: number, arr: number[]): number[][] {
    const len = arr.length;
    let res: number[][] = [];

    let combination = (1 << n) - 1;
    while (combination < (1 << len)) {
        res.push(arr.filter((_, idx) => (combination & (1 << idx)) !== 0));
        // let binaryStr = combination.toString(2);
        // let paddedBinaryStr = binaryStr.padStart(arr.length, '0');
        // res.push(arr.filter((_, idx) => (paddedBinaryStr[idx]) == '1'));

        // Gosper's hack for next combination
        // Find the rightmost 1-bit that has a left 0-bit, then swap them 
        // Move all 1 - bits that are to the right of that bit to the end
        // example 1. 011 -> 101
        // example 2. 101 -> 110
        // example 3. 110 -> 1001 but this would stop the execution

        const rightMostOneBit = combination & -combination;  //011 & 101 = 001
        const leftSide = combination + rightMostOneBit; // 011 + 001 = 100
        const OnesCluster = leftSide ^ combination; // 100 xOr 011 = 111
        // Remove all trailing 0-bits and shift those we don't need
        // But shifting first and then dividing is cheaper
        const rightShiftedBits = (OnesCluster >> 2) / rightMostOneBit;
        combination = leftSide | rightShiftedBits; // 100 OR 001 = 101
    }
    return res;
}

function stringGosperHack(s: string): string {
    // Starts from -1 because if we found only 1 we already swapped it with 0
    let countOnes = -1;
    let lastIdx = s.length - 1
    for (let i = lastIdx; i >= 0; i--) {
        const prev = s[i - 1]
        const curr = s[i]
        if (curr == '1') {
            countOnes++;
        }
        if (curr == '1' && prev == '0') {
            let newString = s.slice(0, i - 1)
            newString += '10'
            newString += '0'.repeat(lastIdx - i - countOnes) + '1'.repeat(countOnes);
            return newString
        }
    }
    // Edge case when there are no sequences of 0 being before 1
    return '10' + '0'.repeat(lastIdx - 1) + '1'.repeat(countOnes);
}

console.log(generateNSizedSets(6, [1, 2, 3, 4, 4, 1, 2, 2]));
console.log(generateNSizedSetsV2(2, [1, 2, 4]));