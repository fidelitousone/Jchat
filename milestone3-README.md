# Testing

## Why did you choose to test the code you did?
### Mocked Unit Tests
#### test_day_command
Tests to make sure that the time of day correctly displays when its invoked
#### test_funtranslate_command
Tests to make sure that funtranslate works and can correctly parse the JSON its given
#### test_funtranslate_command_fail
Tests to make sure that in the event that the API becomes unavailable to the public, the response is proprely parsed
#### test_funtranslate_overuse
Tests to make sure that in the event that the API becomes overused, the response is proprely parsed
#### test_emit_connected_users
Tests to make sure that emit_connected_users is called exactly with the argument it was given, to ensure that the argument isn't somehow being mutated during function execution
#### test_on_connect
Tests to make sure that on_connect() executes without any errors when a user connects to the server.
#### test_new_user
Tests to make sure that test_new_user() executes without any errors and can properly accept any argument, even the one that it was not intended to.
#### test_on_disconnect
Tests to make sure that on_disconnect() executes without error and successfully makes an emit to react when a user disconnects.
#### test_on_new_message
Tests to make sure that when a user sends a message from
the front-end, that flask-socketio receives a mocked json from the front-end and can properly accept it without throwing an error
#### test_new_msg_bot
Tests to make sure that when the user sends a bot invocation to the server, using a mocked json response, that the function can accept the message without throwing an error
#### test_index
Tests to to make sure that when the server first lands on the page that python doesn't throw an error for any reason.

### Unmocked Unit Tests
#### test_about_command
Test to see that invoking the about command returns the proper string
#### test_help_command
Test to see that invoking the help command returns the proper string
#### test_unknown_command
Test to see that invoking the bot with a garbage string that the bot doesn't recognize to be a command returns the unknown command string
#### test_funtranslate_url
Test to see that the bot is using and ONLY using the leetspeak API link to send requests to.
#### test_handle_bot_invoke
Test to see that the main on_message handler can detect when a message has invoked the bot to perform a function, in this case, the about function
#### test_bad_number_command
Edge case test to see that passing a number prompts the bot to return its unknown command function
#### test_bad_number_invoke
Edge case test to see that directly passing a number to the main on_message() invoker returns to the user that the bot was not executed at all due to an error in type
#### test_extra_invoke_cmd
Edge case test to see if adding an extra invoke symbol to the bot breaks it, instead intended response should be that the command is invalid and it doesn't know.
#### test_invoke_passed_to_bot_directly
Edge case test to see if passing the invoke exactly how it is `!!{COMMAND_HERE}` to the bot returns a command not found error.
#### test_invoke_bot_list
Edge case test to see if anything other than a string returns an unknown command, in this case a list is passed directly to the bot.


##  Is there anything else you would like to test if you had the time?
I would test nothing else in bot because it's at 100% coverage, but given more time I would use a better way to mock HTTP requests and also database calls. There are seperate libraries to specifically mock requests and SQLAlchemy, but due to time constraints this wasn't possible. Normal mocking, although not covering everything to 100%, is still good enough.