module.exports = {
    chainWebpack: (config) => {
        config.module
            .rule('images')
            .use('url-loader')
            .tap(options => Object.assign({}, options, {
                name: '[name].[ext]'
            }));
    },
    css: {
        extract: {
            filename: 'css/[name].css',
            chunkFilename: 'css/[name].css',
        },
    },
    configureWebpack: {
        output: {
            filename: 'js/[name].js',
            // chunkFilename: 'js/[id].[name].[chunkhash:8].js',
            chunkFilename: 'js/[name].js',
        }
    }
};