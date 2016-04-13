module.exports = {
    entry: './filterpages/static/filterpages/js/src/main.js',
    output: {
        path: './filterpages/static/filterpages/js/dist',
        filename: 'bundle.js'
    },
    // need to figure out how to enable watch
    //watch: true,
    devtool: 'source-map',
    module: {
        loaders: [
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
                query: {
                    presets: ['es2015']
                }
            }
        ]
    }
}
