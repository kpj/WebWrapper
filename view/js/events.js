/* generic event code */
var Events = new EventEmitter(); 

Events.__pyTrigger = function(evt, args) {
	Events.trigger.apply(Events, [evt, args]); 
}