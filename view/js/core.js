$(document).ready(function() {
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
});