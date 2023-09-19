#!/usr/bin/node
// Searches the second biggest integer in the list of arguments.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  // Extract the integer values and convert them to numbers.
  const numbers = process.argv.slice(2).map(Number);

  if (numbers.some(isNaN)) {
    console.log('Invalid input. Please provide a list of integers.');
  } else {
    // Sort the numbers in descending order numerically.
    const sortedNumbers = numbers.sort((a, b) => b - a);

    console.log(sortedNumbers[1]);
  }
}
