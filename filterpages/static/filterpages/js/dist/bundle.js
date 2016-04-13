/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;
/******/
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	var _arithmetic = __webpack_require__(1);
	
	var result = _arithmetic.operations.add(1, 3);
	console.log(result);
	
	result = _arithmetic.operations.subtract(1, 4);
	console.log(result);
	
	// tutorial1.js
	var CommentBox = React.createClass({
	  displayName: 'CommentBox',
	
	  render: function render() {
	    return React.createElement(
	      'div',
	      { className: 'commentBox' },
	      'Hello, world! I am a CommentBox.'
	    );
	  }
	});
	ReactDOM.render(React.createElement(CommentBox, null), document.getElementById('content'));

/***/ },
/* 1 */
/***/ function(module, exports) {

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

/***/ }
/******/ ]);
//# sourceMappingURL=bundle.js.map