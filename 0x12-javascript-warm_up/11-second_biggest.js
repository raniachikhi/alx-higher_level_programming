#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments
if (process.argv.length <= 2) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(Number);

  if (numbers.some(isNaN)) {
    console.log("Invalid input. Please provide a list of integers.");
  } else {
    const sortedNumbers = numbers.sort((a, b) => b - a);

    console.log(sortedNumbers[1]);
  }
}
