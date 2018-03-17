function Hello(){
	this.hello = function(){
		console.log('Hello');
	};

	this.word = function(){
		console.log('World');
	};
}

module.exports = Hello;
