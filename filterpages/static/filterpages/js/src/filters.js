export var BodyStyle = React.createClass({
  getInitialState: function() {
    return {
      username: '',
      lastGistUrl: '',
      items: [],
    };
  },

  componentDidMount: function() {
    this.serverRequest = $.get(this.props.source, function (result) {
      var lastGist = result[0];
      this.setState({
        username: lastGist.owner.login,
        lastGistUrl: lastGist.html_url,
        items: [],
      });
    }.bind(this));
  },

  componentWillUnmount: function() {
    this.serverRequest.abort();
  },

  render: function() {
      //var createItem = "<li>1</li>"
      var createItem = function() {
        return <li>2</li>;
      };

    return (
      <div>
        {this.state.username}s last gist is
        <a href={this.state.lastGistUrl}>here</a>
        <ul>{this.createItem}</ul>
      </div>
    );
  }
});
