$(document).ready(function() {
	//PyInterface.execute('setWindowTitle', ('My Title'));
	//PyInterface.execute('show', ());

	alert("done");
});

function test() {
	PyInterface.execute('setWindowTitle', ['My Title']);
}