'use strict';

process.env.DEBUG = 'actions-on-google:*';
const App = require('actions-on-google').DialogflowApp;
const functions = require('firebase-functions');


// a. the action name from the make_name Dialogflow intent
const NAME_ACTION = 'make_name';
// b. the parameters that are parsed from the make_name intent
const COLOR_ARGUMENT = 'color';
const NUMBER_ARGUMENT = 'number';


module.exports = async function(context) {
  const app = new App({request: context.request, response: context.response});
  console.log('Request headers: ' + JSON.stringify(context.request.headers));
  console.log('Request body: ' + JSON.stringify(context.request.body));


// c. The function that generates the silly name
  function makeName (app) {
    let number = app.getArgument(NUMBER_ARGUMENT);
    let color = app.getArgument(COLOR_ARGUMENT);


    let message = ''
    if (!color) {
      message = 'You didnt give me a color, i picked one for you!'
      color = 'blue'
    }
    if (!number) {
      message = 'You didnt give me a number, so i generated one for you'
      number = Math.random()
    } else if (isNaN(number)) {
      message = 'The number you gave me doesnt seem like a number, so i generated one for you'
      number = Math.random()
    }

    message += 'Alright, your silly name is ' +
      color + ' ' + number +
      '! I hope you like it. See you next time.'


    app.tell(message);
  }
  // d. build an action map, which maps intent names to functions
  let actionMap = new Map();
  actionMap.set(NAME_ACTION, makeName);


  app.handleRequest(actionMap);
}
