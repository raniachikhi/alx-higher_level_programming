#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    // Check if the arguments are valid, and if not, set width and height to undefined.
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = undefined;
      this.height = undefined;
    }
  }
};
