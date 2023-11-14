#!/usr/bin/node
// A file that modifies the value of myVar to 333

myVar = 333;

101
#!/usr/bin/node
// a function that executes x times a function.

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
