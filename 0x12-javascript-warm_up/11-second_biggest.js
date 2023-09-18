#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  // Extract the integer values and convert them to numbers.
  const numbers = process.argv.slice(2).map(Number);

  // Check if any conversion resulted in NaN (non-numeric input).
  if (numbers.some(isNaN)) {
    console.log("Invalid input. Please provide a list of integers.");
  } else {
    // Sort the numbers in descending order.
    const sortedNumbers = numbers.sort((a, b) => b - a);

    // Output the second largest number.
    console.log(sortedNumbers[1]);
  }
}

