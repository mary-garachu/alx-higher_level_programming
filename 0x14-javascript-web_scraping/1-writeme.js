#!/usr/bin/node

const fs = require('fs');

// Check if both file path and string to write are provided as arguments
if (process.argv.length < 4) {
  console.error('Please provide both a file path and a string to write.');
  process.exit(1);
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`String "${stringToWrite}" has been written to ${filePath}`);
});
