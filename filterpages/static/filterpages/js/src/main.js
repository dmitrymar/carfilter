import {operations} from './arithmetic.js';

let result = operations.add(1, 3);
console.log(result);

result = operations.subtract(1, 4);
console.log(result);

// tutorial1.js
var CommentBox = React.createClass({
  render: function() {
    return (
      <div className="commentBox">
        Hello, world! I am a CommentBox.
      </div>
    );
  }
});
ReactDOM.render(
  <CommentBox />,
  document.getElementById('content')
);
