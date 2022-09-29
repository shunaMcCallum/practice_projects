function findRange(num1, num2) {
    let range = [];
    for (let i = num1; i <= num2; i++) {
        range.push(i);
    }
    return range;
};
    
function primeFinder(n) {
    let range = findRange(2, n);
    let array = [];
    for (number of range) {
        if (number === 2 || number === 3) {
            array.push(number);
        }
        else if (number % 2 === 0 || number % 3 === 0) {
            continue;
        }
        else {
            array.push(number);
        };
    };
    return array;
}

console.log(primeFinder(11))
