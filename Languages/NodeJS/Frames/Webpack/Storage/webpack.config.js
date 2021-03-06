const path = require('path')
//const { CheckerPlugin } = require('awesome-typescript-loader')
const {CleanWebpackPlugin} = require('clean-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
	entry: './src/index.ts',
	output: {
		filename: 'bundle.js',
		path: path.resolve(__dirname, 'dist')
	},
	module: {
		rules: [
			{
				test: /\.tsx?$/,
//				use: 'awesome-typescript-loader',
				use: 'ts-loader',
				exclude: /node_modules/
			}
		]
	},
	plugins: [
		new CleanWebpackPlugin(),
//		new CheckerPlugin()
		new HtmlWebpackPlugin({
			title: 'wmsj100 typescript',
			minify: {
				removeComments: true,
				collapseWhitespace: true,
				minifyCSS: true
			},
			hash: true,
			filename: 'index.html',
//			template: './src/template.html'
		})
	],
	resolve: {
		extensions: ['.tsx', '.ts', '.js']
	}
}
