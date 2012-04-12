// Vimperator Plugin: 'ig'
// Last Change: 26-Aug-2010 
// License: MIT
// Maintainer: Jason Adams <julietmikealpha@gmail.com>
// Usage: Use :ig 
// Usage: if successful you'll be at your iGoogle page ;) 

commands.addUserCommand(['ig'], "Navigate to your iGoogle page",
						function(args) {
							var url = "http://www.google.com/ig";
							liberator.open(url, liberator.CURRENT_TAB);
						});
