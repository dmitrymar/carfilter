
import {BodyStyle} from './filters.js';

ReactDOM.render(
  <BodyStyle source="https://api.github.com/users/octocat/gists" />,
  document.getElementById('content')
);
