function replaceElements(arr: number[]): number[] {
    const n = arr.length;
    let maxRight = -1; // Initialize the rightmost element as -1

    for (let i = n - 1; i >= 0; i--) {
        const currentElement = arr[i];
        arr[i] = maxRight; // Replace the current element with the maximum element on its right
        maxRight = Math.max(maxRight, currentElement); // Update the maximum element on the right
    }

    return arr;
}