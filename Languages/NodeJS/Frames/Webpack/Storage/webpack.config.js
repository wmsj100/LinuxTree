const path = require('path')
//const { CheckerPlugin } = require('awesome-typescript-loader')
const {CleanWebpackPlugin} = require('clean-webpack-plugin')

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
	],
	resolve: {
		extensions: ['.tsx', '.ts', '.js']
	}
}
