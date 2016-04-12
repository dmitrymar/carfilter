"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});
var operations = exports.operations = {
    add: function add(a, b) {
        return a + b;
    },
    subtract: function subtract(a, b) {
        return a - b;
    }
};
'use strict';

var _arithmetic = require('./arithmetic.js');

var result = _arithmetic.operations.add(4, 1);
console.log(result);

result = _arithmetic.operations.subtract(3, 1);
console.log(result);

//# sourceMappingURL=bundle.js.map