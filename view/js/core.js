$(document).ready(function() {
	/*
	 * Setup window/webview
	 */
	PyInterface.execute('window', 'setWindowTitle', ['My Title']);

	struct = [
		{
			"name": "foo",
			"items": [
				{
					"name": "bar",
					"shortcut": "Ctrl+O",
					"statustip": "baz",
					"trigger": "func_name"
				}
			]
		}
	];
	PyInterface.create_menu(JSON.stringify(struct));

	PyInterface.execute('window', 'show', []);

	/*
	 * Setup event handling
	 */
	Events.on('func_name', function(e) {
		alert('Event handled');
	});
});