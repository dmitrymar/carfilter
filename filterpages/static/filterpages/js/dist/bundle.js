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
	
	var _filters = __webpack_require__(1);
	
	ReactDOM.render(React.createElement(_filters.BodyStyle, { source: 'https://api.github.com/users/octocat/gists' }), document.getElementById('content'));

/***/ },
/* 1 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	var BodyStyle = exports.BodyStyle = React.createClass({
	  displayName: 'BodyStyle',
	
	  getInitialState: function getInitialState() {
	    return {
	      username: '',
	      lastGistUrl: '',
	      items: []
	    };
	  },
	
	  componentDidMount: function componentDidMount() {
	    this.serverRequest = $.get(this.props.source, function (result) {
	      var lastGist = result[0];
	      this.setState({
	        username: lastGist.owner.login,
	        lastGistUrl: lastGist.html_url,
	        items: []
	      });
	    }.bind(this));
	  },
	
	  componentWillUnmount: function componentWillUnmount() {
	    this.serverRequest.abort();
	  },
	
	  render: function render() {
	    //var createItem = "<li>1</li>"
	    var createItem = function createItem() {
	      return React.createElement(
	        'li',
	        null,
	        '2'
	      );
	    };
	
	    return React.createElement(
	      'div',
	      null,
	      this.state.username,
	      's last gist is',
	      React.createElement(
	        'a',
	        { href: this.state.lastGistUrl },
	        'here'
	      ),
	      React.createElement(
	        'ul',
	        null,
	        this.createItem
	      )
	    );
	  }
	});

/***/ }
/******/ ]);
//# sourceMappingURL=bundle.js.map